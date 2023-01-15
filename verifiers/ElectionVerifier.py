import hashlib

from helios_verifier.verifiers.VoteVerifier import verify_vote
from helios_verifier.Util.HashUtil import sha256_b64_decoded, sha256_b64


def verify_partial_decryption_proof(ciphertext, decryption_factor, proof, public_key):
    # Here, we prove that (g, y, ciphertext.alpha, decryption_factor) is a DDH tuple, proving knowledge of secret key x.
    # Before we were working with (g, alpha, y, beta/g^m), proving knowledge of the random factor r.
    if pow(public_key.g, proof.response, public_key.p) != (
            (proof.commitment.A * pow(public_key.y, proof.challenge, public_key.p)) % public_key.p):
        return False

    if pow(ciphertext.alpha, proof.response, public_key.p) != (
            (proof.commitment.B * pow(decryption_factor, proof.challenge, public_key.p)) % public_key.p):
        return False

    # compute the challenge generation, Fiat-Shamir style
    str_to_hash = str(proof.commitment.A) + "," + str(proof.commitment.B)
    computed_challenge = hashlib.sha256(str_to_hash)

    # check that the challenge matches
    return computed_challenge == proof.challenge


def retally_election(election, voters, result, ballots):
    # compute the election fingerprint
    election_fingerprint = sha256_b64_decoded(election)

    # keep track of voter fingerprints
    vote_fingerprints = []

    # keep track of running tallies, initialize at 0
    # again, assuming operator overloading for homomorphic addition
    tallies = [[0 for a in question.answers] for question in election.questions]

    # go through each voter, check it
    for voter in voters:
        cast_vote = 0
        for ballot in ballots:
            if ballot.voter_uuid == voter.uuid:
                cast_vote = ballot
                break
        if cast_vote == 0:
            return False
        if not verify_vote(election, cast_vote.vote):
            return False

        # compute fingerprint
        vote_fingerprints.append(sha256_b64(voter))

        # update tallies, looping through questions and answers within them
        for question_num in range(len(election.questions)):
            for choice_num in range(len(election.questions[question_num].answers)):
                tallies[question_num][choice_num] = voter.vote.answers[question_num].choices[choice_num] + \
                                                    tallies[question_num][choice_num]

    # now we have tallied everything in ciphertexts, we must verify proofs
    for question_num in range(len(election.questions)):
        for choice_num in range(len(election.questions[question_num].answers)):
            decryption_factor_combination = 1

            for trustee_num in range(len(election.trustees)):
                trustee = election.trustees[trustee_num]

                # verify the tally for that choice within that question
                # check that it decrypts to the claimed result with the claimed proof
                if not verify_partial_decryption_proof(tallies[question_num][choice_num],
                                                       trustee.decryption_factors[question_num][choice_num],
                                                       trustee.decryption_proof[question_num][choice_num],
                                                       trustee.public_key):
                    return False

                # combine the decryption factors progressively
                decryption_factor_combination *= trustee.decryption_factors[question_num][choice_num]
                if (decryption_factor_combination * election.result[question_num][
                    choice_num]) % election.public_key.p != tallies[question_num][
                    choice_num].beta % election.public_key.p:
                    return False

    # return the complete tally, now that it is confirmed
    return {
        'election_fingerprint': election_fingerprint,
        'vote_fingerprints': vote_fingerprints,
        'verified_tally': result
    }
