from datetime import datetime


class AccountHistory:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transactions.append({
            "type": transaction.type,
            "value": transaction.value,
            "date": datetime.now(),
        })
