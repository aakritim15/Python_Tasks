class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is Rs. {self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Rs. {amount} deposited successfully. Your new balance is Rs. {self.balance}"
        else:
            return "Invalid deposit amount. Please enter a positive number."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Rs. {amount} withdrawn successfully. Your new balance is Rs. {self.balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount."
        else:
            return "Insufficient funds. Withdrawal failed."

if __name__ == "__main__":
    atm = ATM()
    while True:
        print("\nATM Simulator!!")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice : ")

        if choice == '1':
            print(atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter the deposit amount: Rs. "))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter the withdrawal amount: Rs. "))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("Thank you!")
            break
        else:
            print("Invalid choice.")
