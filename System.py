class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance  # Encapsulation

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):  # Inheritance
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print(f"Interest Added: ₹{interest:.2f}")


class ATM:
    def __init__(self, account):
        self.account = account

    def menu(self):
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Add Interest")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                print("Balance: ₹", self.account.get_balance())

            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                self.account.deposit(amount)

            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                self.account.withdraw(amount)

            elif choice == "4":
                self.account.add_interest()

            elif choice == "5":
                print("Thank you for using ATM!")
                break

            else:
                print("Invalid Choice")


# Main Program
account = SavingsAccount(
    account_number="12345",
    holder_name="Sujith",
    balance=5000,
    interest_rate=5
)

atm = ATM(account)
atm.menu()
