import re


class Bank:
    def __init__(self):
        self.balance = 0
        self.withdraw_number = 0
        self.WITHDRAW_LIMIT = 3
        self.statement = []
        self.limit = 500

        self.USER_DB = []

        self.ACCOUNT_DB = []
        self.bank_agency = '001'
        self.bank_account = 1

    def main(self):
        menu = """
    
        [1] Deposit
        [2] Withdraw
        [3] Statement
        [4] Create User
        [5] Create Account
        [6] List Accounts
        [7] Exit
    
        => """

        while True:

            option = int(input(menu))

            if option == 1:
                value = float(input("Insert the deposit value: "))
                self.deposit(value)

            elif option == 2:
                value = float(input("Insert the value to withdraw: "))

                self.withdraw(value)

            elif option == 3:
                self.get_statement()

            elif option == 4:
                username = str(input("Insert your username: "))
                document = str(input("Insert your document: "))

                self.create_user(username, document)
            elif option == 5:
                document = str(input("Insert your document: "))

                self.create_account(document)
            elif option == 6:
                account_number = int(input("Insert your account number: "))

                self.filter_account(account_number)

            else:
                print("Invalid option, please select other option.")

    def deposit(self, value):
        if value > 0:
            self.balance += value
            self.statement.append(f"Deposit:  $ +{value:.2f}")
        else:
            print("You insert a invalid value.")

    def withdraw(self, value):
        if value > self.limit:
            print(f"Failure! Exceeded withdraw limit, the limit is {self.limit}.")

        elif value > self.balance:
            print(f"Failure! You don't have this balance. Your balance is $ {value:.2f}.")

        elif self.withdraw_number >= self.WITHDRAW_LIMIT:
            print("Failure! You can't do more withdraw, you reach at a limit.")

        elif value > 0:
            self.balance -= value
            self.statement.append(f"Withdraw: $ -{value:.2f}")
            self.withdraw_number += 1

        else:
            print("Failure! You insert a invalid value.")

    def get_statement(self):
        print("\n================ Statement ================")
        print("There are no movements." if not self.statement else "\n".join(self.statement))
        print(f"\nBalance: $ {self.balance:.2f}")
        print("=" * 50)

    def create_user(self, username, document):
        if not self.filter_user(document):
            print('Create user with success.')
            self.USER_DB.append({'user_name': username, 'document': document})
            return

        print("User already exists.")

    def filter_user(self, document):
        document = re.sub(r'[^\w\s]', '', document)
        return [item for item in self.USER_DB if item['document'] == document]

    def create_account(self, document):
        user = self.filter_user(document)
        if user:
            user = user[0]
            print(f'Create account with success.\nAgency: {self.bank_agency}\nAccount: {self.bank_account}')
            self.ACCOUNT_DB.append({'bank_agency': self.bank_agency,
                                    'account_number': self.bank_account,
                                    'user_name': user['user_name'],
                                    'document': document,
                                    })
            self.bank_account += 1
            return
        print('User not found.')

    def filter_account(self, account_number):
        account = [item for item in self.ACCOUNT_DB if item['account_number'] == account_number]

        if account:
            line = f'''
                Agency:\t{self.bank_agency}
                Account Number:\t{account_number}
                Owner:\t{account[0]['user_name']}     
            '''
            print("=" * 50)
            print(line)


Bank().main()
