from helios_verifier.util.HashUtil import hex_sha1


def verify_partial_decryption_proof(ciphertext, decryption_factor, proof, public_key):
    """
    Protocol verifying that the given decryption factor decrypts to the claimed result with the
    claimed proof. This means proving that (public_key.g, public_key.y, ciphertext.alpha, decryption_factor)
    is a DDH tuple and therefore proving the knowledge of the secret key.

    :param ciphertext: ciphertext of an encrypted answer (choice)
    :param decryption_factor: decryption_factor corresponding to the encrypted choice
    :param proof: ZKProof corresponding to the encrypted choice
    :param public_key: public_key of the election
    :return: bool, False if the discrete logs are not equal or the challenges do not match, True otherwise
    """
    if pow(public_key.g, proof.response, public_key.p) != (
            (proof.commitment.A * pow(public_key.y, proof.challenge, public_key.p)) % public_key.p):
        return False

    if pow(ciphertext.alpha, proof.response, public_key.p) != (
            (proof.commitment.B * pow(decryption_factor, proof.challenge, public_key.p)) % public_key.p):
        return False

    # compute the challenge generation, Fiat-Shamir style
    str_to_hash = str(proof.commitment.A) + "," + str(proof.commitment.B)
    computed_challenge = hex_sha1(str_to_hash)

    # check that the challenge matches
    return int.from_bytes(computed_challenge, "big") == proof.challenge
