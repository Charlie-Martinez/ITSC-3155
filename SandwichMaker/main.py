### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient,amount_needed in ingredients.items():
            if self.machine_resources[ingredient] < amount_needed:
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")

        large_dollars = int(input("How many large dollars?: "))
        half_dollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))

        total = (large_dollars * 1.0) + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, amount_needed in order_ingredients.items():
            self.machine_resources[ingredient] -= amount_needed

### Make an instance of SandwichMachine class and write the rest of the codes ###
machine = SandwichMachine(resources)

while True:
    sandwich_size = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if sandwich_size == "off":
        print("Machine has been powered off.")
        break
    elif sandwich_size == "report":
        print(f"Bread: {machine.machine_resources['bread']} slice(s)")
        print(f"Ham: {machine.machine_resources['ham']} slice(s)")
        print(f"Cheese: {machine.machine_resources['cheese']} ounce(s)")
    elif sandwich_size in ["small", "medium", "large"]:
        ingredients_needed = recipes[sandwich_size]["ingredients"]
        cost = recipes[sandwich_size]["cost"]

        if not machine.check_resources(ingredients_needed):
            print(f"Sorry there is not enough ingredients.")
        else:
            coins = machine.process_coins()

            if machine.transaction_result(coins, cost):
                machine.make_sandwich(sandwich_size, ingredients_needed)
                print(f"{sandwich_size} sandwich is ready. Bon appetit!")
    else:
        print("Invalid input, try again.")
