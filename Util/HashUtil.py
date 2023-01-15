import base64
import hashlib


def sha256_b64(helios_object):
    string_encoded_json_object = helios_object.to_json(separators=(',', ':')).encode()
    hashed_json_object = hashlib.sha256(string_encoded_json_object)
    base64_encoded_hash = base64.b64encode(hashed_json_object.digest())
    return base64_encoded_hash
