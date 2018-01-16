import hashlib

class Block:
    def __init__(self, data, timestamp, prevHash):
        self.data = data
        self.timestamp = timestamp
        self.prevHash = prevHash
        self.contents = [data, timestamp, prevHash]

        self.blockHash = self.sha256_hash(self.contents)

    def sha256_hash(self, c):
        c = str(c)
        #double hashing
        inner_hash = hashlib.sha256(c.encode()).hexdigest()
        outer_hash = hashlib.sha256(inner_hash.encode()).hexdigest()
        return outer_hash
