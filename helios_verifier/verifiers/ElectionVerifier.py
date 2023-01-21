from helios_verifier.verifiers.VoteVerifier import verify_vote
from helios_verifier.verifiers.DecryptionFactorVerifier import verify_partial_decryption_proof
from helios_verifier.domain.ElGamalCiphertext import ElGamalCiphertext
from helios_verifier.util.HashUtil import sha256_b64


def retally_election(election, voters, result, ballots, trustees):
    """
    Protocol for the verification of a whole election. This means verifying the votes of all the voters,
    verifying the overall election result and proving for the trustees the knowledge of the secret keys
    used in the election.
    :param election: election to be verified
    :param voters: voters that casted a vote in the election
    :param result: overall election result
    :param ballots: cast votes to be verified
    :param trustees: trustees responsible for generating the key pairs used in the election. They ned to proof
        the knowledge of the secret keys
    :return: bool, True if verification of all components succeeded, False otherwise
    """

    # keep track of voter fingerprints
    vote_fingerprints = []

    # keep track of running tallies
    tallies = [[ElGamalCiphertext(1, 1) for a in question.answers] for question in election.questions]

    # go through each voter, check it
    for voter in voters:
        cast_vote = 0
        for ballot in ballots:
            if ballot.voter_uuid == voter.uuid:
                cast_vote = ballot
                break
        if cast_vote == 0:
            break
        if not verify_vote(election, cast_vote.vote):
            return False

        # compute fingerprint
        vote_fingerprints.append(sha256_b64(voter))

        # update tallies, looping through questions and answers within them
        for question_num in range(len(election.questions)):
            for choice_num in range(len(election.questions[question_num].answers)):
                tallies[question_num][choice_num].alpha = \
                    (cast_vote.vote.answers[question_num].choices[choice_num].alpha *
                     tallies[question_num][choice_num].alpha) % election.public_key.p
                tallies[question_num][choice_num].beta = \
                    (cast_vote.vote.answers[question_num].choices[choice_num].beta *
                     tallies[question_num][choice_num].beta) % election.public_key.p

    # now we have tallied everything in ciphertexts, we must verify proofs
    for question_num in range(len(election.questions)):
        for choice_num in range(len(election.questions[question_num].answers)):
            decryption_factor_combination = 1

            for trustee_num in range(len(trustees)):
                trustee = trustees[trustee_num]

                # verify the tally for that choice within that question
                # check that it decrypts to the claimed result with the claimed proof
                if not verify_partial_decryption_proof(tallies[question_num][choice_num],
                                                       trustee.decryption_factors[question_num][choice_num],
                                                       trustee.decryption_proofs[question_num][choice_num],
                                                       trustee.public_key):
                    return False

                # combine the decryption factors progressively
                decryption_factor_combination *= trustee.decryption_factors[question_num][choice_num]
                if (decryption_factor_combination *
                    pow(election.public_key.g, result[question_num][choice_num], election.public_key.p)) \
                        % election.public_key.p \
                        != tallies[question_num][choice_num].beta % election.public_key.p:
                    return False

    return True
