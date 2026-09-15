import json


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
            print("Insufficient funds")

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
            "account_type": self.__class__.__name__,
            "balance": self.balance,
            "history": self.history
        }


class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 0.05

        self.balance += interest

        self.history.append(
            f"Interest added: R{interest:.2f}"
        )

        print(
            f"Interest added: R{interest:.2f}"
        )


class BusinessAccount(BankAccount):
    def apply_monthly_fee(self):
        fee = 50

        if self.balance >= fee:
            self.balance -= fee

            self.history.append(
                f"Monthly fee charged: R{fee:.2f}"
            )

            print(
                f"Monthly fee charged: R{fee:.2f}"
            )
        else:
            print("Insufficient funds for monthly fee.")


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

                account_type = info.get(
                    "account_type",
                    "BankAccount"
                )

                if account_type == "SavingsAccount":
                    account = SavingsAccount(name)

                elif account_type == "BusinessAccount":
                    account = BusinessAccount(name)

                else:
                    account = BankAccount(name)

                account.balance = info.get(
                    "balance",
                    0.0
                )

                account.history = info.get(
                    "history",
                    []
                )

                accounts[name] = account

    except FileNotFoundError:
        pass

    return accounts


def create_account(accounts):
    name = input("Enter account name: ")

    if name in accounts:
        print("Account already exists.")
        return

    print("\n1. Savings Account")
    print("2. Business Account")

    account_type = input(
        "Choose account type: "
    )

    if account_type == "1":
        accounts[name] = SavingsAccount(name)

    elif account_type == "2":
        accounts[name] = BusinessAccount(name)

    else:
        print("Invalid account type.")
        return

    print(f"Account '{name}' created.")


def list_accounts(accounts):
    if not accounts:
        print("No accounts found.")
    else:
        print("\n=== Accounts ===")

        for name, account in accounts.items():
            print(
                f"{name} "
                f"({account.__class__.__name__})"
            )


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

    target_name = input(
        "Transfer to account: "
    )

    if target_name not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(
            input("Transfer amount: ")
        )

        current_account.transfer(
            accounts[target_name],
            amount
        )

    except ValueError:
        print(
            "Please enter a valid amount."
        )


def add_interest(current_account):
    if isinstance(
        current_account,
        SavingsAccount
    ):
        current_account.add_interest()

    else:
        print(
            "Only Savings Accounts can earn interest."
        )


def apply_fee(current_account):
    if isinstance(
        current_account,
        BusinessAccount
    ):
        current_account.apply_monthly_fee()

    else:
        print(
            "Only Business Accounts have monthly fees."
        )


def main():
    accounts = load_accounts()
    current_account = None

    while True:
        print("\n=== Bank App V4 ===")

        if current_account:
            print(
                f"Current Account: {current_account.owner}"
            )
            print(
                f"Type: {current_account.__class__.__name__}"
            )
            print(
                f"Balance: R{current_account.balance:.2f}"
            )

        print("\n1. Create Account")
        print("2. List Accounts")
        print("3. Select Account")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Transfer")
        print("7. Add Interest")
        print("8. Apply Fee")
        print("9. View Balance")
        print("10. View History")
        print("11. Save Accounts")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            list_accounts(accounts)

        elif choice == "3":
            current_account = select_account(accounts)

        elif choice == "4":
            if current_account is None:
                print("Select an account first.")
                continue

            try:
                amount = float(input("Deposit amount: "))
                current_account.deposit(amount)
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "5":
            if current_account is None:
                print("Select an account first.")
                continue

            try:
                amount = float(input("Withdrawal amount: "))
                current_account.withdraw(amount)
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "6":
            transfer_money(accounts, current_account)

        elif choice == "7":
            add_interest(current_account)

        elif choice == "8":
            apply_fee(current_account)

        elif choice == "9":
            if current_account is None:
                print("Select an account first.")
            else:
                current_account.show_balance()

        elif choice == "10":
            if current_account is None:
                print("Select an account first.")
            else:
                current_account.show_history()

        elif choice == "11":
            save_accounts(accounts)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()