#This class is the network between wallets
#This will do untill I implement a database
class Node:
    def __init__(self, wallets):
        self.wallets = wallets

    def add_wallet(self, wallet):
        self.wallets.append(wallet)

    def add_wallets(self, wallets):
        for wallet in wallets:
            self.add_wallet(walelt)
