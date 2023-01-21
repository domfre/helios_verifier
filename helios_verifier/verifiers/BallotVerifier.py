from helios_verifier.verifiers.VoteVerifier import verify_vote


def verify_ballot_audit(vote_with_plaintexts, election):
    """
    Verifies a vote and if it was properly encrypted. First calls :meth:`verify_vote` to verify
    the proofs. For each encrypted answer it is then checked whether the ciphertexts of all the possible
    choices are properly generated with the randomness used for this election.
    :param vote_with_plaintexts: cast vote of a voter with the encrypted answer accompanied with the
        respective plaintexts
    :param election: represents the election the ballot was cast for
    :return: bool indicating whether the verification succeeded or not
    """
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
