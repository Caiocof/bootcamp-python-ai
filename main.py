import re
import textwrap
from datetime import datetime

import transaction
from account import CheckingAccount
from client import Client
from transaction import Deposit, Withdraw


class Bank:
    @staticmethod
    def _menu():
        options = """
        ===========
        [1] Deposit
        [2] Withdraw
        [3] Statement
        [4] Create User
        [5] Create Account
        [6] List Accounts
        [7] Exit
        ===========> """
        return int(input(options))

    def main(self):
        clients = []
        accounts = []

        while True:

            option = self._menu()

            if option == 1:
                self.transaction(clients, 'deposit')

            elif option == 2:
                self.transaction(clients, 'withdraw')

            elif option == 3:
                self.get_statement(clients)

            elif option == 4:
                self.create_user(clients)
            elif option == 5:
                account_number = len(accounts) + 1

                self.create_account(account_number, clients, accounts)
            elif option == 6:
                self._list_accounts(accounts)

            else:
                print("Invalid option, please select other option.")

    def create_account(self, account_number, clients, accounts):
        account, client = self._get_client_and_account(clients, False)
        if not client:
            return
        account = CheckingAccount.new_account(number=account_number, client=client)
        accounts.append(account)
        client.accounts.append(account)
        print("\n=== Account created successfully. ===")

    def transaction(self, clients, type_transaction):
        account, client = self._get_client_and_account(clients)

        if not account or not client:
            return

        transaction = None
        if type_transaction == "deposit":
            value = float(input("Insert the deposit value: "))
            transaction = Deposit(value)
        elif type_transaction == "withdraw":
            value = float(input("Insert the withdraw value: "))
            transaction = Withdraw(value)

        if account and transaction:
            client.add_transaction(account, transaction)

    def get_statement(self, clients):
        account, client = self._get_client_and_account(clients)

        if not account or not client:
            return

        print("\n================ Statement ================")
        transactions = account.history.transactions
        message = ""
        if not transactions:
            message = "No transactions yet"
        else:
            items = [f"\n{item.type}:\n\tR$ {item.value:.2f}" for item in transactions]
            message = "".join(items)

        print(message)
        print(f"\nBalance: \n\tR$ {account.balance:.2f}")
        print("======================================")

    def _get_client_and_account(self, clients, check_account=True):
        document = input("Insert your documento number: ")
        client = self._filter_client(document, clients)
        account = None

        if not client:
            print("Sorry, the client does not exist.")
            return account, client

        account = self._filter_account_by_client(client)
        if not account and check_account:
            print("Sorry, the account does not exist.")
            return account, client

        return account, client

    @staticmethod
    def _filter_client(document, clients):
        document = re.sub(r'[^\w\s]', '', document)
        find_client = [client for client in clients if client.document == document]
        return find_client[0] if find_client else None

    @staticmethod
    def _filter_account_by_client(client):
        if not client.accounts:
            return

        accounts = [f'[{index}] : {account.number}' for index, account in enumerate(client.accounts)]
        accounts = "\n".join(accounts)

        choose_account = int(input(f"""Select account:
        ===========
        {accounts}
        ===========> """))

        return client.accounts[choose_account]

    @staticmethod
    def _list_accounts(accounts):
        for account in accounts:
            print("=" * 50)
            print(textwrap.dedent(str(account)))

    def create_user(self, clients):
        document = input("Insert your documento number: ")
        client = self._filter_client(document, clients)
        if client:
            print("Sorry, Client already exists.")

        name = input("Insert your name: ")
        birthday = input("Insert your birthday (YYYY-MM-DD): ")

        client = Client(document=document, name=name,
                        birth_date=datetime.strptime(birthday, '%Y-%m-%d'))
        clients.append(client)


Bank().main()
