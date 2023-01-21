"""
verifiers.BallotVerifier
~~~~~~~~~~~~~~~~~~~~~~~~
helios_verifier
:author: Dominik Frey
"""
from helios_verifier.verifiers.VoteVerifier import verify_vote


def verify_ballot_audit(vote_with_plaintexts, election):
    public_key = election.public_key
    # check the proofs
    if not verify_vote(election, vote_with_plaintexts):
        return False

    # check the proper encryption of each choice within each question
    # go through each encrypted answer
    for encrypted_answer in vote_with_plaintexts.answers:

        # loop through each choice by integer (multiple arrays)
        for choice_num in range(len(encrypted_answer.choices)):

            # the ciphertext and randomness used to encrypt it
            ciphertext = encrypted_answer.choices[choice_num]
            randomness = encrypted_answer.randomness[choice_num]

            # the plaintext we expect, g^1 if selected, or g^0 if not selected
            if choice_num == encrypted_answer.answer:
                plaintext = public_key.g
            else:
                plaintext = 1

            # check alpha
            if pow(public_key.g, randomness, public_key.p) != ciphertext.alpha:
                return False

            # check beta
            expected_beta = (pow(public_key.y, randomness, public_key.p) * plaintext) % public_key.p
            if expected_beta != ciphertext.beta:
                return False

    return True
