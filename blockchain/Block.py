import datetime
import hashlib

class Block:
    def __init__(self, data, timestamp, prevHash):
        self.prevHash = prevHash
        self.data = data
        self.timestamp = timestamp
        self.contents = [data, timestamp, prevHash]

        self.blockHash = sha256_hash(contents)

    def sha256_hash(self, c):
        c = str(c)
        inner_hash = hashlib.sha256(c.encode()).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash

    @staticmethod
    def genesis_block():
        return Block ("The very first block", datetime.datetime.now(), "0")
