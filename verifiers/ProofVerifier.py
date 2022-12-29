import hashlib


def verify_proof(ciphertext, plaintext, proof, public_key):
    if pow(public_key.g, proof.response, public_key.p) != (
            (proof.commitment.A * pow(ciphertext.alpha, proof.challenge, public_key.p)) % public_key.p):
        return False
    beta_over_m = pow(pow(public_key.g, plaintext, public_key.p), -1, public_key.p) * ciphertext.beta
    beta_over_m_mod_p = beta_over_m % public_key.p
    if pow(public_key.y, proof.response, public_key.p) != (
            (proof.commitment.B * pow(beta_over_m_mod_p, proof.challenge, public_key.p)) % public_key.p):
        return False
    return True


def verify_disjunctive_0_max_proof(ciphertext, max, disjunctive_proof, public_key):
    for i in range(max + 1):
        # the proof for plaintext "i"
        if not verify_proof(ciphertext, i, disjunctive_proof[i], public_key):
            return False

    # the overall challenge
    computed_challenge = sum([proof.challenge for proof in disjunctive_proof]) % public_key.q

    # concatenate the arrays of A,B values
    list_of_values_to_hash = sum([[p.commitment.A, p.commitment.B] for p in disjunctive_proof], [])

    # concatenate as strings
    str_to_hash = ",".join(list_of_values_to_hash)

    # hash
    expected_challenge = hashlib.sha1(str_to_hash)

    # last check
    return computed_challenge == expected_challenge
