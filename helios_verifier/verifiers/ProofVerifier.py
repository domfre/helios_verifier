from helios_verifier.util.HashUtil import hex_sha1


def verify_proof(ciphertext, plaintext, proof, public_key):
    """
    Verification of an individual non-interactive proof according to the Chaum-Pedersen
    protocol that the corresponding ciphertext encodes the integer given by the plaintext

    :parameter ciphertext: ElGamalCiphertext
    :parameter plaintext: plain value encoded by the ciphertext
    :parameter proof: (Chaum-Pedersen-) ZkProof for the plaintext encoded by the ciphertext
    :parameter public_key: public_key of the election
    :returns bool indicating whether the validation succeeded or not
    """
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
    """
    Verifies a list of max disjunctive zero-knowledge proofs, one for each possible value
    of the plaintext between 0 and max. The challenges of all the single zero-knowledge proofs must
    sum up to the actual challenge of the protocol to ensure that there is one real proof whereas
    the others are simulated

    :parameter ciphertext: ElGamalCiphertext
    :parameter max: maximum value that the ciphertext encodes (a ciphertext encodes a value between o and max)
    :parameter disjunctive_proof: list[ZkProof], one for each value between 0 and max
    :parameter public_key: public_key of the election
    :returns bool indicating whether validation succeeded or not
    """
    for i in range(max + 1):
        # the proof for plaintext "i"
        if not verify_proof(ciphertext, i, disjunctive_proof[i], public_key):
            return False

    # the overall challenge
    computed_challenge = sum([proof.challenge for proof in disjunctive_proof]) % public_key.q

    # concatenate the arrays of A,B values
    list_of_values_to_hash = sum([[p.commitment.A, p.commitment.B] for p in disjunctive_proof], [])

    # concatenate as strings
    str_to_hash = ",".join([str(value) for value in list_of_values_to_hash])

    # hash
    expected_challenge = hex_sha1(str_to_hash)

    # last check
    return computed_challenge == int.from_bytes(expected_challenge, "big")
