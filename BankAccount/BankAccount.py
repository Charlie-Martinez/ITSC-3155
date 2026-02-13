class BankAccount:
    bank_title = "Bank of America"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance += amount
        print(f"Deposit has been successful, new current balance: {self.current_balance}\n")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: This is not a valid amount to withdraw\n")
        elif (self.current_balance - amount) < self.minimum_balance:
            print("Error: This withdraw would put you under the minimum balance\n")
        else:
            self.current_balance -= amount
            print(f"Withdrawal has been successful, new current balance: {self.current_balance}\n")

    def print_customer_information(self):
        return (f"Bank Name: {self.bank_title}\n"
                f"Customer Name: {self.customer_name}\n"
                f"Current Balance: {self.current_balance}\n"
                f"Minimum Balance: {self.minimum_balance}\n")

act1 = BankAccount("John", 100, 100)
print(act1.print_customer_information())
act1.deposit(100)
print(act1.print_customer_information())

act2 = BankAccount("Mary", 800, 500)
print(act2.print_customer_information())
act2.withdraw(0)
act2.withdraw(1000)
print(act2.print_customer_information())