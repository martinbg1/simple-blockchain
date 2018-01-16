from Block import Block
import datetime
import random
import time

genesis_block = Block("The very first block", datetime.datetime.now(), "0")
blockchain = [genesis_block]

print("Genesis block   : ", blockchain[0].contents)
print("\t\t", blockchain[0].blockHash, "\n")

while True:
    #creates a new block every 5 seconds
    time.sleep(5)
    #the data in this example is just a random number between 1 and 1000000
    blockchain.append(Block(random.randint(1, 1000000), datetime.datetime.now(), blockchain[len(blockchain)-2].blockHash))
    print("Block number ", len(blockchain), ": ", blockchain[len(blockchain)-1].contents)
    print("\t\t", blockchain[len(blockchain)-1].blockHash, "\n")
