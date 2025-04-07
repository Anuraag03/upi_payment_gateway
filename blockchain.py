import hashlib
import time

class Block:
    def __init__(self, transaction_id, previous_hash, timestamp=None):
        self.transaction_id = transaction_id
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.hash = self.compute_hash()

    def compute_hash(self):
        data = f"{self.transaction_id}{self.previous_hash}{self.timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "hash": self.hash
        }

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block("0"*64, "0"*64, time.time())
        self.chain.append(genesis_block)

    def add_block(self, transaction_id):
        last_block = self.chain[-1]
        new_block = Block(transaction_id, last_block.hash)
        self.chain.append(new_block)
        return new_block.to_dict()
    
    def _save_block_to_db(self, block):
        self.cursor.execute('''
            INSERT INTO blockchain (transaction_id, previous_hash, timestamp, hash)
            VALUES (?, ?, ?, ?)
        ''', (block.transaction_id, block.previous_hash, block.timestamp, block.hash))
        self.conn.commit()

    def get_chain(self):
        return [block.to_dict() for block in self.chain]

