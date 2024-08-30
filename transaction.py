from abc import ABC, abstractmethod

from account import Account


class Transaction(ABC):

    @property
    @abstractmethod
    def value(self):
        pass

    @abstractmethod
    def register(self, account: Account):
        pass


class Withdraw(Transaction):
    def __init__(self, value):
        self._value = value
        self._type = 'withdraw'

    @property
    def value(self):
        return self._value

    @property
    def type(self):
        return self._type

    def register(self, account: Account):
        transaction = account.withdraw(self.value)

        if transaction:
            account.history.add_transaction(self)


class Deposit(Transaction):
    def __init__(self, value):
        self._value = value
        self._type = 'deposit'

    @property
    def value(self):
        return self._value

    @property
    def type(self):
        return self._type

    def register(self, account: Account):
        transaction = account.deposit(self.value)
        if transaction:
            account.history.add_transaction(self)
