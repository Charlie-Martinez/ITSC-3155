# BAD TIP CALCULATOR - Violating best practices
# Violations: No KISS, No Single Responsibility, No Clean Code, Violates DRY

def calculate_tip():
    # Everything in one giant function - violates Single Responsibility
    print("=" * 40)
    print("TIP CALCULATOR")
    print("=" * 40)

    # Getting inputs
    bill = float(input("Enter your bill amount: $"))
    tip_percent = float(input("Enter tip percentage (e.g., 15, 18, 20): "))
    people = int(input("How many people splitting? "))

    # Calculate tip - but we repeat this logic later!
    tip_amount = bill * (tip_percent / 100)

    # Calculate total with tip
    total_with_tip = bill + tip_amount

    # Calculate per person - but we calculate this twice!
    per_person = total_with_tip / people

    # Display results with messy formatting
    print("\n" + "=" * 30)
    print("YOUR BILL BREAKDOWN")
    print("=" * 30)
    print(f"Original Bill: ${bill}")
    print(f"Tip ({tip_percent}%): ${tip_amount}")
    print(f"Total: ${total_with_tip}")
    print(f"Each Person Pays: ${per_person}")

    # Redundant calculation - violates DRY!
    # This is the SAME calculation we did above
    check_total = bill + (bill * (tip_percent / 100))
    if check_total != total_with_tip:
        print("Warning: Math doesn't match!")  # This will never happen

    # More redundant code - calculating per person AGAIN
    check_per_person = check_total / people
    print(f"Just to double-check: ${check_per_person} each")

    # Extra feature nobody asked for - violates YAGNI
    if total_with_tip > 100:
        print("\n⭐ Big spender! ⭐")
        print("Here's a coupon for your next meal!")
        print("(This feature wasn't requested but I added it anyway)")

    # Another unnecessary feature
    if tip_percent >= 20:
        print("You're a generous tipper! 🌟")
    elif tip_percent <= 10:
        print("Um, that's a bit low... 😬")


# Single function does EVERYTHING
# Hard to test
# Hard to modify
# Hard to read
# Violates: KISS, Single Responsibility, DRY, Clean Code, YAGNI

if __name__ == "__main__":
    calculate_tip()