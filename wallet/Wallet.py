from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

class Wallet:
    def __init__(self,balance):
        self.balance = balance

        self.raw_key = rsa.generate_private_key(backend=crypto_default_backend(),public_exponent=65537,key_size=512)
        self.publicKey = self.generate_publicKey(self.raw_key)
        #Not safe to store privateKey here. This is meant as a demonstration
        self.privateKey = self.generate_privateKey(self.raw_key)


    def generate_publicKey(self, key):
        publicKey = key.public_key().public_bytes(crypto_serialization.Encoding.OpenSSH,crypto_serialization.PublicFormat.OpenSSH)
        return publicKey

    def generate_privateKey(self, key):
        privateKey = key.private_bytes(crypto_serialization.Encoding.PEM,crypto_serialization.PrivateFormat.PKCS8,crypto_serialization.NoEncryption())
        return privateKey

#    def transaction(privateKey, publicKey):

        #FILL

    def check_privateKey(self, privateKey):
        return privateKey == self.privateKey


test_wallet = Wallet(100)
test_walelt_2 = Wallet(500000)
#Again, not safe to have access to the privateKey this way
print(test_wallet.publicKey, "\n\n", test_wallet.privateKey, "\n\n")
print(test_walelt_2publicKey, "\n\n", test_walelt_2.privateKey, "\n\n")
