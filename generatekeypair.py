# import secrets
# from tinyec import registry
#
# curve = registry.get_curve('curve25519')
#
#
# def compress_point(point):
#     return hex(point.x) + hex(point.y % 2)[2:]
#
#
# privKey = secrets.randbelow(curve.field.n)
# pubKey = privKey * curve.g
#
# print("private key:", hex(privKey))
# print("public key:", compress_point(pubKey))

# from securesystemslib.interface import import_ed25519_publickey_from_file, \
#     generate_and_write_ed25519_keypair_with_prompt
#
# generate_and_write_ed25519_keypair_with_prompt('ed25519_key')
#
# public_ed25519_key = import_ed25519_publickey_from_file('ed25519_key.pub')

import securesystemslib
import nacl.encoding
import nacl.signing

signing_key = nacl.signing.SigningKey.generate()
print("this is the signing key: ", signing_key)

import nacl.utils
from nacl.public import PrivateKey, Box

skB = PrivateKey.generate()
print("this is the private key: ", skB)

pkbob = skB.public_key
print("this is the public key: ", pkbob)
