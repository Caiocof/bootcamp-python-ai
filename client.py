from datetime import date


class Client:
    _accounts: list
    _document: str
    _name: str
    _birth_date: date

    def __init__(self, document: str, name: str, birth_date: date):
        self._accounts = []
        self._document = document
        self._name = name
        self._birth_date = birth_date

    @property
    def name(self) -> str:
        return self._name

    @property
    def document(self) -> str:
        return self._document

    @property
    def accounts(self) -> list:
        return self._accounts

    @staticmethod
    def add_transaction(account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self._accounts.append(account)
        return account
