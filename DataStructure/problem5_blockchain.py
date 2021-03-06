import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        sha.update(self.data.encode('utf-8'))

        return sha.hexdigest()


class Node:
    def __init__(self, block):
        self.block = block
        self.previous = None


class BlockChain:
    def __init__(self):
        self.first_block = None
        self.last_block = None

    def append(self, value=None):
        if self.first_block is None:
            self.first_block = Node(self.create_genesis_block(value))
            self.last_block = self.first_block
        else:
            new_block = Node(self.next_block(self.last_block.block.previous_hash, value))
            new_block.previous = self.last_block
            self.last_block = new_block

    def create_genesis_block(self, value):
        return Block(datetime.now(), "Hey! I'm Genesis Block " + value, "0")

    def next_block(self, previous_hash, value):
        this_timestamp = datetime.now()
        this_data = "" if not value else "Hey! I'm block {}".format(value)
        this_hash = previous_hash
        return Block(this_timestamp, this_data, this_hash)

    def get_last_block(self):
        return self.last_block


# Test case 1
print('---Test case 1---')
chain = BlockChain()
chain.append('111')
chain.append('222')
chain.append('333')
chain.append('444')
chain.append('555')
chain.append('666')
chain.append('777')
chain.append('888')
chain.append('999')

last_block = chain.get_last_block()
while(last_block):
    print(last_block.block.data)
    last_block = last_block.previous

# Test case 2
print('---Test case 2---')
chain = BlockChain()
chain.append('111')
chain.append('999')

last_block = chain.get_last_block()
while(last_block):
    print(last_block.block.data)
    last_block = last_block.previous

# Test case 3
print('---Test case 3---')
chain = BlockChain()
chain.append('111')
chain.append()

while(last_block):
    print(last_block.block.data)
    last_block = last_block.previous
