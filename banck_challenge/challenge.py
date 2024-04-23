menu = """

[1] Deposit
[2] Withdraw
[3] Statement
[4] Exit

=> """

balance = 0
limit = 500
statement = []
withdraw_number = 0
WITHDRAW_LIMIT = 3

while True:

    option = int(input(menu))

    if option == 1:
        value = float(input("Insert the deposit value: "))

        if value > 0:
            balance += value
            statement.append(f"Deposit:  $ +{value:.2f}")

        else:
            print("You insert a invalid value.")

    elif option == 2:
        value = float(input("Insert the value to withdraw: "))

        if value > limit:
            print(f"Failure! Exceeded withdraw limit, the limit is {limit}.")

        elif value > balance:
            print(f"Failure! You don't have this balance. Your balance is $ {value:.2f}.")

        elif withdraw_number >= WITHDRAW_LIMIT:
            print("Failure! You can't do more withdraw, you reach at a limit.")

        elif value > 0:
            balance -= value
            statement.append(f"Withdraw: $ -{value:.2f}")
            withdraw_number += 1

        else:
            print("Failure! You insert a invalid value.")

    elif option == 3:
        print("\n================ Statement ================")
        print("There are no movements." if not statement else "\n".join(statement))
        print(f"\nBalance: $ {balance:.2f}")
        print("==========================================")

    elif option == 4:
        break

    else:
        print("Invalid option, please select other option.")
