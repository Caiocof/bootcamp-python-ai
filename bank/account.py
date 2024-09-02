from account_history import AccountHistory
from client import Client


class Account:

    def __init__(self, number: int, client: Client):
        self._balance: float = 0
        self._number: int = number
        self._bank_account: str = "0001"
        self._client: Client = client
        self._history = AccountHistory()

    @classmethod
    def new_account(cls, number: int, client: Client):
        return cls(number, client)

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def number(self) -> int:
        return self._number

    @property
    def bank_account(self) -> str:
        return self._bank_account

    @property
    def client(self) -> Client:
        return self._client

    @property
    def history(self):
        return self._history

    def withdraw(self, value: float) -> bool:
        if value > self.balance:
            print(f"\nFailure! You don't have this balance. Your balance is $ {self.balance:.2f}.")

        elif value > 0:
            self._balance -= value
            print(f"\nSuccess! You now have $ {self._balance:.2f}.")
            return True

        else:
            print("Failure! You insert a invalid value.")

        return False

    def deposit(self, value: float) -> bool:
        if value > 0:
            self._balance += value
            print(f"\nSuccess! You now have $ {self._balance:.2f}.")
            return True
        else:
            print("Failure! You insert a invalid value.")

        return False


class CheckingAccount(Account):
    def __init__(self, number: int, client: Client, limit=500, withdraw_limit=3):
        super().__init__(number, client)
        self.limit = limit
        self.withdraw_limit = withdraw_limit

    def withdraw(self, value: float) -> bool:
        withdraws = [transaction for transaction in self.history.transactions if transaction["type"] == "withdraw"]

        if value > self.limit:
            print(f"Failure! Exceeded withdraw limit, the limit is {self.limit}.")

        elif len(withdraws) >= self.withdraw_limit:
            print("Failure! You can't do more withdraw, you reach at a limit.")
        else:
            return super().withdraw(value)

        return False

    def __str__(self):
        return f"""
        Bank Account:\t{self.bank_account}
        Number:\t\t{self.number}
        Withdraw Limit:\t{self.withdraw_limit}
        Owner:\t{self.client.name}
        """
