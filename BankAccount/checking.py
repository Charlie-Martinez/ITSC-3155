from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.__account_number = account_number
        self._routing_number = routing_number
        self.transfer_limit = transfer_limit

    def get_account_number(self):
        return self.__account_number

    def print_customer_information(self):
        customer_info = super().print_customer_information()
        return (f"{customer_info}\n"
                f"Account Type: Checking\n"
                f"Account Number: {self.__account_number}\n"
                f"Routing Number: {self._routing_number}\n")