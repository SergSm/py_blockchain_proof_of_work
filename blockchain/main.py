import hashlib
import json
from time import time


class Blockchain(object):
    """Class used to store a blockchain
    and have a helper method to add new blocks to the chain """

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Creates the genesis block
        self.new_block(proof=100, previous_hash=1)

    def new_block(self, proof, previous_hash=None):
        """Creates a new Block ands adds it to the chain

        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous block
        :return: <dict> New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to go into the next mined Block

        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            }
        )

        # After adding a transaction to the list this function
        # returns the index of the block
        # which the transaction will be added to the next one to be mined
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block

        :param block: <dict> Block
        :return: <str>
        """

        # We must make sure that the Dictionary is Ordered,
        # or we will have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Returns the last Block in the chain"""
        return self.chain[-1]
