
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from math import ceil

# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/dh/

class BlufiCrypto(object):
    def __init__(self, generator: int = 2, key_size: int = 512):
        # Generate necessary keys
        self.dh_param = dh.generate_parameters(generator=generator, key_size=key_size)
        self.pn = self.dh_param.parameter_numbers()
        self.p = self.pn.p
        self.g = self.pn.g
        self.privKey = self.dh_param.generate_private_key()
        self.pubKey = self.privKey.public_key()
        self.y = self.pubKey.public_numbers().y

    def genKeys(self):
        # Already generated in __init__()
        return

    def bytewidth(self, param):
        return ceil(param.bit_length() / 8)

    def deriveSharedKey(self, peer_pub_bytes):
        y = int.from_bytes(peer_pub_bytes, "big")
        peer_public_numbers = dh.DHPublicNumbers(y, self.pn)
        peer_public_key = peer_public_numbers.public_key()
        shared_key = self.privKey.exchange(peer_public_key)
        digest = hashes.Hash(hashes.MD5())
        digest.update(shared_key)
        return digest.finalize()

    def getPBytes(self):
        return self.p.to_bytes(self.bytewidth(self.p), "big")

    def getGBytes(self):
        return self.g.to_bytes(self.bytewidth(self.g), "big")

    def getYBytes(self):
        return self.y.to_bytes(self.bytewidth(self.y), 'big')
