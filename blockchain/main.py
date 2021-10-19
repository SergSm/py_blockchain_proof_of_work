

class Blockchain:
    """Class used to store a blockchain
    and have a helper method to add new blocks to the chain """

    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        """Creates a new Block ands adds it to the chain"""
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the list of transactions

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
        """Hashes a block"""
        pass

    @property
    def last_block(self):
        """Returns the last Block in the chain"""
        pass
