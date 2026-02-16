from savings import SavingsAccount
from checking import CheckingAccount

def main():
    # Creating instances to test
    savings_test = SavingsAccount("John", 100, 100, 123456789, 987654321, 0.02)
    print(savings_test.print_customer_information())
    savings_test.deposit(100)
    print(savings_test.print_customer_information())
    savings_test.apply_interest()
    print(savings_test.print_customer_information())

    print("\n \n")

    checking_test = CheckingAccount("Mary", 800, 500, 234567890, 987654321, 400)
    print(checking_test.print_customer_information())
    checking_test.withdraw(0)
    checking_test.withdraw(1000)
    print(checking_test.print_customer_information())
    checking_test.transfer(1000)
    checking_test.transfer(-200)
    checking_test.transfer(400)
    checking_test.transfer(100)
    print(checking_test.print_customer_information())

main()