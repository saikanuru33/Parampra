class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def get_price(self):
        # Calculate price based on size and number of toppings
        # Add your pricing logic here
        price_per_topping = 1.5
        base_price = 8
        topping_cost = len(self.toppings) * price_per_topping
        total_price = base_price + topping_cost
        return total_price

class Order:
    def __init__(self, customer, pizzas):
        self.customer = customer
        self.pizzas = pizzas

    def get_total_price(self):
        # Calculate the total price of the order
        total_price = 0
        for pizza in self.pizzas:
            total_price += pizza.get_price()
        return total_price

    def display_order(self):
        # Display order details
        print("Order for:", self.customer)
        print("Pizzas:")
        for i, pizza in enumerate(self.pizzas, start=1):
            print(f"Pizza {i}: {pizza.size} inch with {', '.join(pizza.toppings)}")
        print("Total price:", self.get_total_price())

# Example usage
if __name__ == "__main__":

	pizza1 = Pizza(12, ["Pepperoni", "Mushrooms"])
	pizza2 = Pizza(10, ["Ham", "Pineapple"])
	order = Order("John Doe", [pizza1, pizza2])
	order.display_order()
