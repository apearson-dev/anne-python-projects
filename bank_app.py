import json


def load_data():
    try:
        with open("bank_data.json", "r") as file:
            data = json.load(file)
            return data.get("balance", 0.0), data.get("history", [])

    except FileNotFoundError:
        return 0.0, []


def save_data(balance, history):
    data = {
        "balance": balance,
        "history": history
    }

    with open("bank_data.json", "w") as file:
        json.dump(data, file, indent=4)


def deposit(balance, history):
    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Amount must be positive.")

        else:
            balance += amount

            history.append(
                f"Deposit: R{amount:.2f} | Balance: R{balance:.2f}"
            )

            print(f"New balance: R{balance:.2f}")

    except ValueError:
        print("Invalid amount.")

    return balance


def withdraw(balance, history):
    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Amount must be positive.")

        elif amount <= balance:
            balance -= amount

            history.append(
                f"Withdrawal: R{amount:.2f} | Balance: R{balance:.2f}"
            )

            print("Withdrawal successful")
            print(f"New balance: R{balance:.2f}")

        else:
            print("Insufficient funds")

    except ValueError:
        print("Invalid amount.")

    return balance


def show_balance(balance):
    print(f"Current balance: R{balance:.2f}")


def show_history(history):
    print("\n=== Transaction History ===")

    if not history:
        print("No transactions found.")

    else:
        for transaction in history:
            print(transaction)


def main():
    balance, history = load_data()

    while True:
        print("\n=== Python Bank ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            balance = deposit(balance, history)

        elif choice == "2":
            balance = withdraw(balance, history)

        elif choice == "3":
            show_balance(balance)

        elif choice == "4":
            show_history(history)

        elif choice == "5":
            save_data(balance, history)
            print("Bank data saved.")
            print("Thank you for using Python Bank!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()