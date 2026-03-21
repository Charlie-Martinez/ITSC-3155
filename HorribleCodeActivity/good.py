"""
A simple tip calculator demonstrating coding best practices.

This module calculates tips, totals, and split amounts for restaurant bills.
It follows KISS, DRY, and Single Responsibility principles.
"""


def calculate_tip(bill_amount, tip_percentage):
    """
    Calculate tip amount based on bill and tip percentage.

    Args:
        bill_amount (float): The original bill amount
        tip_percentage (float): Tip percentage (e.g., 15 for 15%)

    Returns:
        float: The calculated tip amount
    """
    return bill_amount * (tip_percentage / 100)


def calculate_total(bill_amount, tip_amount):
    """
    Calculate total bill including tip.

    Args:
        bill_amount (float): The original bill amount
        tip_amount (float): The tip amount

    Returns:
        float: Total bill with tip included
    """
    return bill_amount + tip_amount


def split_bill(total_amount, number_of_people):
    """
    Split total bill among specified number of people.

    Args:
        total_amount (float): The total bill amount
        number_of_people (int): Number of people splitting

    Returns:
        float: Amount each person pays
    """
    return total_amount / number_of_people


def format_currency(amount):
    """
    Format a number as currency with 2 decimal places.

    Args:
        amount (float): The amount to format

    Returns:
        str: Formatted currency string (e.g., "$15.99")
    """
    return f"${amount:.2f}"


def display_bill_summary(bill, tip_percent, tip_amount, total, per_person):
    """
    Display formatted bill summary to user.

    Args:
        bill (float): Original bill amount
        tip_percent (float): Tip percentage
        tip_amount (float): Calculated tip
        total (float): Total with tip
        per_person (float): Amount per person
    """
    print("\n" + "=" * 35)
    print("BILL SUMMARY")
    print("=" * 35)
    print(f"Original Bill:    {format_currency(bill)}")
    print(f"Tip ({tip_percent}%):        {format_currency(tip_amount)}")
    print(f"Total with Tip:   {format_currency(total)}")
    print(f"Each Person Pays: {format_currency(per_person)}")
    print("=" * 35)


def get_positive_number(prompt):
    """
    Get a positive number input from user with validation.

    Args:
        prompt (str): The input prompt to display

    Returns:
        float: Valid positive number entered by user
    """
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_positive_integer(prompt):
    """
    Get a positive integer input from user with validation.

    Args:
        prompt (str): The input prompt to display

    Returns:
        int: Valid positive integer entered by user
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive whole number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    """
    Main program function orchestrating the tip calculator flow.

    Each function has a single responsibility, making the code:
    - Easy to test independently
    - Simple to modify or extend
    - Clear and readable (KISS principle)
    - Reusable (DRY principle)
    """
    print("=" * 40)
    print("WELCOME TO THE TIP CALCULATOR")
    print("=" * 40)

    # Get user inputs with validation
    bill_amount = get_positive_number("Enter your bill amount: $")
    tip_percentage = get_positive_number("Enter tip percentage (e.g., 15, 18, 20): ")
    number_of_people = get_positive_integer("How many people are splitting? ")

    # Perform calculations using separate functions
    tip_amount = calculate_tip(bill_amount, tip_percentage)
    total_amount = calculate_total(bill_amount, tip_amount)
    per_person_amount = split_bill(total_amount, number_of_people)

    # Display results
    display_bill_summary(
        bill_amount,
        tip_percentage,
        tip_amount,
        total_amount,
        per_person_amount
    )

    print("\nThank you for using the Tip Calculator!")


if __name__ == "__main__":
    main()