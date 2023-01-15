from helios_verifier.verifiers.ProofVerifier import verify_disjunctive_0_max_proof
from helios_verifier.Util.HashUtil import sha256_b64


def verify_vote(election, vote):
    # check hash (remove the last character which is a useless '=')
    computed_hash = sha256_b64(election)[:-1].decode()
    if computed_hash != vote.election_hash:
        return False

    # go through each encrypted answer by index, because we need the index
    # into the question array, too for figuring out election information
    for question_num in range(len(vote.answers)):
        encrypted_answer = vote.answers[question_num]
        question = election.questions[question_num]

        # initialize homomorphic sum (assume operator overload on __add__ with 0 special case.)
        homomorphic_sum = 0

        # go through each choice for the question (loop by integer because two arrays)
        for choice_num in range(len(encrypted_answer.choices)):
            ciphertext = encrypted_answer.choices[choice_num]
            disjunctive_proof = encrypted_answer.individual_proofs[choice_num]

            # check the individual proof (disjunctive max is 1)
            if not verify_disjunctive_0_max_proof(ciphertext, 1, disjunctive_proof, election.public_key):
                return False

            # keep track of homomorphic sum
            homomorphic_sum = ciphertext + homomorphic_sum

        # check the overall proof
        if not verify_disjunctive_0_max_proof(homomorphic_sum, question.max, encrypted_answer.overall_proof,
                                              election.public_key):
            return False

    # done, we succeeded
    return True
