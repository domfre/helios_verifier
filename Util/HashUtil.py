import base64
import hashlib


def sha256_b64(helios_object):
    string_encoded_json_object = helios_object.to_json(separators=(',', ':')).encode('utf-8')
    hashed_json_object = hashlib.sha256(string_encoded_json_object)
    base64_encoded_hash = base64.b64encode(hashed_json_object.digest())
    return base64_encoded_hash


def sha256_b64_decoded(helios_object):
    string_encoded_json_object = helios_object.to_json(separators=(',', ':')).encode('utf-8')
    hashed_json_object = hashlib.sha256(string_encoded_json_object)
    base64_encoded_hash = base64.b64encode(hashed_json_object.digest())
    return base64_encoded_hash.decode('ascii')


def sha256_b64_trimmed(helios_object):
    string_encoded_json_object = helios_object.to_json(separators=(',', ':')).encode('utf-8')
    hashed_json_object = hashlib.sha256(string_encoded_json_object)
    base64_encoded_hash = base64.b64encode(hashed_json_object.digest())
    return base64_encoded_hash[:-1]


def sha256_b64_trimmed_and_decoded(helios_object):
    string_encoded_json_object = helios_object.to_json(separators=(',', ':')).encode('utf-8')
    hashed_json_object = hashlib.sha256(string_encoded_json_object)
    base64_encoded_hash = base64.b64encode(hashed_json_object.digest())
    return base64_encoded_hash[:-1].decode('ascii')


def sha256(string_object):
    return hashlib.sha256(string_object.encode())
