from Node import Node
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

class Wallet:
    def __init__(self, balance):
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

    def transaction(self, recv_publicKey, sender_privateKey, amount, node_wallets):
        flag = False
        if self.check_privateKey(sender_privateKey) and amount >= self.balance:
            print("pending...")
            for wallet in node_wallets:
                if recv_publicKey == wallet.publicKey:
                    self.balance -= amount
                    wallet.balance += amount
                    print("transaction conpleted. Sent ", amount, " to ", wallet.publicKey)
                    flag = True
                    break
        if not flag:
            print("Transaction failed...")

    def check_privateKey(self, privateKey):
        return self.privateKey == privateKey

#test wallets
test_wallet = Wallet(100)
test_walelt_2 = Wallet(500000)
node = Node([test_wallet, test_walelt_2])
#Again, not safe to have access to the privateKey this way
#public key and private key test
print(test_wallet.publicKey, "\n\n", test_wallet.privateKey, "\n\n")
print(test_walelt_2.publicKey, "\n\n", test_walelt_2.privateKey, "\n\n")
#transaction test
print(test_wallet.balance, "\t", test_walelt_2.balance)
test_wallet.transaction("Failed attempt", test_wallet.privateKey, 100, node.wallets)
print(test_wallet.balance, "\t", test_walelt_2.balance, "\n\n")
test_wallet.transaction(test_walelt_2.publicKey, test_wallet.privateKey, 100, node.wallets)
print(test_wallet.balance, "\t", test_walelt_2.balance)
