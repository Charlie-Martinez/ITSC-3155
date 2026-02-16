from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.__account_number = account_number
        self._routing_number = routing_number
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.current_balance += (self.current_balance * self.interest_rate)
        print(f"Interest applied. New current balance: {self.current_balance}\n")

    def get_account_number(self):
        return self.__account_number

    def print_customer_information(self):
        customer_info = super().print_customer_information()
        return (f"{customer_info}"
                f"Account Type: Savings\n"
                f"Account Number: {self.__account_number}\n"
                f"Routing Number: {self._routing_number}\n")