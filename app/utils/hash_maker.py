from hashlib import pbkdf2_hmac
from os import getenv, urandom


class HashMaker:
    @staticmethod
    def create_hash(password: str):
        sha_256_iterations: int = 100000
        hash_limit_byte: int = 128
        print(getenv('PASSWORD_HASH_SALT'))
        return pbkdf2_hmac(
            hash_name='sha256',
            password=password.encode('utf-8'),
            salt=int(getenv('PASSWORD_HASH_SALT')),
            iterations=sha_256_iterations,
            dklen=hash_limit_byte
        )
