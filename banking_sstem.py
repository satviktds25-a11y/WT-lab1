from datetime import datetime

# MODULE 1: Account Management

accounts = {}


def create_account():
    print("\n--- CREATE ACCOUNT ---")

    acc = input("Enter account number: ")

    if acc in accounts:
        print("Account already exists!")
        return

    name = input("Enter account holder name: ")
    pin = input("Set 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("PIN must be 4 digits!")
        return

    accounts[acc] = {
        "name": name,
        "pin": pin,
        "balance": 0.0,
        "history": []
    }

    print("Account created successfully!")


def verify_account():
    acc = input("Enter account number: ")

    if acc not in accounts:
        print("Account not found!")
        return None

    pin = input("Enter PIN: ")

    if accounts[acc]["pin"] != pin:
        print("Incorrect PIN!")
        return None

    return acc


# MODULE 2: Deposit and Withdrawal

def deposit():
    acc = verify_account()

    if acc is None:
        return

    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Enter a positive amount!")
            return

        accounts[acc]["balance"] += amount

        accounts[acc]["history"].append(
            ("Deposit", amount, str(datetime.now()))
        )

        print("Deposit successful!")

    except ValueError:
        print("Invalid amount!")


def withdraw():
    acc = verify_account()

    if acc is None:
        return

    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Enter a positive amount!")
            return

        if amount > accounts[acc]["balance"]:
            print("Insufficient balance!")
            return

        accounts[acc]["balance"] -= amount

        accounts[acc]["history"].append(
            ("Withdrawal", amount, str(datetime.now()))
        )

        print("Withdrawal successful!")

    except ValueError:
        print("Invalid amount!")


# MODULE 3: Transfer and Balance Enquiry

def transfer():
    sender = verify_account()

    if sender is None:
        return

    receiver = input("Enter receiver account number: ")

    if receiver not in accounts:
        print("Receiver account not found!")
        return

    if sender == receiver:
        print("Cannot transfer to the same account!")
        return

    try:
        amount = float(input("Enter transfer amount: "))

        if amount <= 0:
            print("Enter a positive amount!")
            return

        if amount > accounts[sender]["balance"]:
            print("Insufficient balance!")
            return

        accounts[sender]["balance"] -= amount
        accounts[receiver]["balance"] += amount

        date = str(datetime.now())

        accounts[sender]["history"].append(
            ("Transfer Sent to " + receiver, amount, date)
        )

        accounts[receiver]["history"].append(
            ("Transfer Received from " + sender, amount, date)
        )

        print("Transfer successful!")

    except ValueError:
        print("Invalid amount!")


def check_balance():
    acc = verify_account()

    if acc is None:
        return

    print("Account Holder:", accounts[acc]["name"])
    print("Account Number:", acc)
    print("Available Balance: Rs.", accounts[acc]["balance"])


# MODULE 4: Transaction History and Statement

def transaction_history():
    acc = verify_account()

    if acc is None:
        return

    print("\n--- TRANSACTION HISTORY ---")

    if not accounts[acc]["history"]:
        print("No transactions found!")
        return

    for item in accounts[acc]["history"]:
        print("Type:", item[0])
        print("Amount: Rs.", item[1])
        print("Date:", item[2])
        print("------------------------")


def account_statement():
    acc = verify_account()

    if acc is None:
        return

    print("\n===== ACCOUNT STATEMENT =====")
    print("Account Holder:", accounts[acc]["name"])
    print("Account Number:", acc)
    print("Current Balance: Rs.", accounts[acc]["balance"])

    print("\nTransaction Details:")

    if not accounts[acc]["history"]:
        print("No transactions found!")
    else:
        for item in accounts[acc]["history"]:
            print(item[0], "| Rs.", item[1], "|", item[2])

    # Save statement in a text file
    try:
        filename = "statement_" + acc + ".txt"

        with open(filename, "w") as file:
            file.write("BANK ACCOUNT STATEMENT\n")
            file.write("Name: " + accounts[acc]["name"] + "\n")
            file.write("Account Number: " + acc + "\n")
            file.write(
                "Balance: Rs. " +
                str(accounts[acc]["balance"]) + "\n"
            )

            for item in accounts[acc]["history"]:
                file.write(
                    str(item[0]) + " | Rs. " +
                    str(item[1]) + " | " +
                    str(item[2]) + "\n"
                )

        print("Statement saved to:", filename)

    except OSError:
        print("Statement displayed, but file saving is unavailable.")


# MAIN MENU

def main():
    while True:
        print("\n==============================")
        print(" BANKING MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Funds")
        print("5. Check Balance")
        print("6. Transaction History")
        print("7. Account Statement")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
        elif choice == "5":
            check_balance()
        elif choice == "6":
            transaction_history()
        elif choice == "7":
            account_statement()
        elif choice == "8":
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()