import base64
from .VoteVerifier import verify_vote


def verify_ballot_audit(vote_with_plaintexts, election, vote_fingerprint):
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

    # check the fingerprint
    vote_without_plaintexts = vote_with_plaintexts.remove_plaintexts()
    computed_fingerprint = base64.b64encode(hash.new(vote_without_plaintexts.toJSON()).digest())[:-1]
    return computed_fingerprint == vote_fingerprint
