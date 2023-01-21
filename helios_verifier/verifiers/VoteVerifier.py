from helios_verifier.verifiers.ProofVerifier import verify_disjunctive_0_max_proof
from helios_verifier.domain.ElGamalCiphertext import ElGamalCiphertext


def verify_vote(election, vote):
    """
    Verifies a vote by iteration through all questions. For each question, a 0...max zero-knowledge
    proof is performed via :meth:`verify_disjunctive_0_max_proof` for every possible answer (choice)
    of the question. An overall-proof is then performed on the homomorphic sum of all the ciphertexts.

    :param election: election to verify the votes for
    :param vote: CastVote of a voter that is to be verified
    :return: bool indicating whether the verification succeeded or not
    """
    # go through each encrypted answer by index, because we need the index
    # into the question array, too for figuring out election information
    for question_num in range(len(vote.answers)):
        encrypted_answer = vote.answers[question_num]
        question = election.questions[question_num]

        # initialize homomorphic sum (assume operator overload on __add__ with 0 special case.)
        homomorphic_product = ElGamalCiphertext(1, 1)

        # go through each choice for the question (loop by integer because two arrays)
        for choice_num in range(len(encrypted_answer.choices)):
            ciphertext = encrypted_answer.choices[choice_num]
            disjunctive_proof = encrypted_answer.individual_proofs[choice_num]

            # check the individual proof (disjunctive max is 1)
            if not verify_disjunctive_0_max_proof(ciphertext, 1, disjunctive_proof, election.public_key):
                return False

            # keep track of homomorphic product
            homomorphic_product.alpha = (ciphertext.alpha * homomorphic_product.alpha) % election.public_key.p
            homomorphic_product.beta = (ciphertext.beta * homomorphic_product.beta) % election.public_key.p

        # check the overall proof
        if not verify_disjunctive_0_max_proof(homomorphic_product, question.max, encrypted_answer.overall_proof,
                                              election.public_key):
            return False

    # done, we succeeded
    return True
