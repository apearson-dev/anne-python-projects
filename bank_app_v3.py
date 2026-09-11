import json
import builtins


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

            self.history.append(
                f"{self.owner} deposited R{amount:.2f}"
            )

            print(f"New balance: R{self.balance:.2f}")

        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")

        elif amount > self.balance:
            builtins.print("Insufficient funds")

        else:
            self.balance -= amount

            self.history.append(
                f"{self.owner} withdrew R{amount:.2f}"
            )

            print(f"New balance: R{self.balance:.2f}")

    def transfer(self, target_account, amount):
        if amount <= 0:
            print("Amount must be positive.")

        elif amount > self.balance:
            print("Insufficient funds")

        else:
            self.balance -= amount
            target_account.balance += amount

            self.history.append(
                f"Transferred R{amount:.2f} to {target_account.owner}"
            )

            target_account.history.append(
                f"Received R{amount:.2f} from {self.owner}"
            )

            print(
                f"Transferred R{amount:.2f} "
                f"to {target_account.owner}"
            )

    def show_balance(self):
        print(f"Current balance: R{self.balance:.2f}")

    def show_history(self):
        print(f"\n=== {self.owner}'s Transaction History ===")

        if not self.history:
            print("No transactions found.")
        else:
            for transaction in self.history:
                print(transaction)

    def to_dict(self):
        return {
            "owner": self.owner,
            "balance": self.balance,
            "history": self.history
        }


def save_accounts(accounts):
    data = {}

    for name, account in accounts.items():
        data[name] = account.to_dict()

    with open("accounts.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Accounts saved.")


def load_accounts():
    accounts = {}

    try:
        with open("accounts.json", "r") as file:
            data = json.load(file)

            for name, info in data.items():
                owner = info.get("owner", name)

                account = BankAccount(owner)

                account.balance = info.get("balance", 0.0)
                account.history = info.get("history", [])

                accounts[name] = account

    except FileNotFoundError:
        pass

    return accounts


def create_account(accounts):
    name = input("Enter account name: ")

    if name in accounts:
        print("Account already exists.")

    else:
        accounts[name] = BankAccount(name)
        print(f"Account '{name}' created.")


def list_accounts(accounts):
    if not accounts:
        print("No accounts found.")

    else:
        print("\n=== Accounts ===")

        for name in accounts:
            print(name)


def select_account(accounts):
    name = input("Enter account name: ")

    if name in accounts:
        print(f"Selected account: {name}")
        return accounts[name]

    print("Account not found.")
    return None


def transfer_money(accounts, current_account):
    if current_account is None:
        print("Select an account first.")
        return

    target_name = input("Transfer to account: ")

    if target_name not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Transfer amount: "))

        current_account.transfer(
            accounts[target_name],
            amount
        )

    except ValueError:
        print("Please enter a valid amount.")


def main():
    accounts = load_accounts()
    current_account = None

    while True:
        print("\n=== Bank App V3 ===")

        if current_account:
            print(
                f"Current Account: {current_account.owner}"
            )
            print(
                f"Balance: R{current_account.balance:.2f}"
            )

        print("1. Create Account")
        print("2. Select Account")
        print("3. List Accounts")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. View Balance")
        print("7. View History")
        print("8. Transfer")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            current_account = select_account(accounts)

        elif choice == "3":
            list_accounts(accounts)

        elif choice == "4":
            if current_account:
                try:
                    amount = float(
                        input("Deposit amount: ")
                    )

                    current_account.deposit(amount)

                except ValueError:
                    print(
                        "Please enter a valid amount."
                    )

            else:
                print("Select an account first.")

        elif choice == "5":
            if current_account:
                try:
                    amount = float(
                        input("Withdrawal amount: ")
                    )

                    current_account.withdraw(amount)

                except ValueError:
                    print(
                        "Please enter a valid amount."
                    )

            else:
                print("Select an account first.")

        elif choice == "6":
            if current_account:
                current_account.show_balance()

            else:
                print("Select an account first.")

        elif choice == "7":
            if current_account:
                current_account.show_history()

            else:
                print("Select an account first.")

        elif choice == "8":
            transfer_money(
                accounts,
                current_account
            )

        elif choice == "9":
            save_accounts(accounts)
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()