import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    while True:
        sandwich_size = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if sandwich_size == "off":
            print("Machine has been powered off.")
            break
        elif sandwich_size == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounce(s)")
        elif sandwich_size in ["small", "medium", "large"]:
            ingredients_needed = recipes[sandwich_size]["ingredients"]
            cost = recipes[sandwich_size]["cost"]

            if not sandwich_maker_instance.check_resources(ingredients_needed):
                print(f"Sorry there is not enough ingredients.")
            else:
                coins = cashier_instance.process_coins()

                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(sandwich_size, ingredients_needed)
                    print(f"{sandwich_size} sandwich is ready. Bon appetit!")
        else:
            print("Invalid input, try again.")

if __name__=="__main__":
    main()
