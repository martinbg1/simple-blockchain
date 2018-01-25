from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

class Wallet:
    def __init__(balance):
        self.balance = balance

        self.key = rsa.generate_private_key(backend=crypto_default_backend(),public_exponent=65537,key_size=2048)
        self.publicKey = generate_publicKey(key)
        self.privateKey = generate_privateKey(key)


    def generate_publicKey(key):
        publicKey = key.public_key().public_bytes(crypto_serialization.Encoding.OpenSSH,crypto_serialization.PublicFormat.OpenSSH)
        return publicKey

    def generate_privateKey(key):
        privateKey = key.private_bytes(crypto_serialization.Encoding.PEM,crypto_serialization.PrivateFormat.PKCS8,crypto_serialization.NoEncryption())
        return privateKey
'''
    def transaction(privateKey, publicKey):

        #FILL

    def check_privateKey():

        #FILL
'''
test = Walllet(100)
print(test.publicKey)
