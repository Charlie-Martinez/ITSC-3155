from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.__account_number = account_number
        self._routing_number = routing_number
        self.transfer_limit = transfer_limit

    def transfer(self, amount):
        if amount > self.transfer_limit:
            print(f"Error: Transfer limit exceeded\n")
            return False
        elif (self.current_balance - amount) < self.minimum_balance:
            print(f"Error: This would put you under the minimum balance\n")
            return False
        elif amount <= 0:
            print(f"Error: Invalid amount\n")
            return False
        else:
            self.current_balance -= amount
            print(f"Transfer complete. New current balance: {self.current_balance}\n")
            return True

    def get_account_number(self):
        return self.__account_number

    def print_customer_information(self):
        customer_info = super().print_customer_information()
        return (f"{customer_info}"
                f"Account Type: Checking\n"
                f"Account Number: {self.__account_number}\n"
                f"Routing Number: {self._routing_number}\n")