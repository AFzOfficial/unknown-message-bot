import hashlib


def md5_hash(string: str) -> str:
    return hashlib.md5(f"{string}".encode('utf-8')).hexdigest()