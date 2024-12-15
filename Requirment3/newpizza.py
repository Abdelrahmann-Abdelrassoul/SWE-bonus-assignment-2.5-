from abc import ABC, abstractmethod

# Singleton Inventory Manager
class InventoryManager:
    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InventoryManager, cls).__new__(cls)

        return cls._instance
    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory
    
# Abstract Base Pizza Class
class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

# Pizza Related Classes
class Margherita(Pizza):
    def __init__(self):
        self.description = "Margherita"
        self.cost = 5.0

    def get_description(self) -> str:
        return self.description

    def get_cost(self) -> float:
        return self.cost

class Pepperoni(Pizza):
    def __init__(self):
        self.description = "Pepperoni"
        self.cost = 6.0

    def get_description(self) -> str:
        return self.description

    def get_cost(self) -> float:
        return self.cost
    
# Abstract Base Topping Decorator Class
class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

# Topping Decorator Related Classes
class Cheese(ToppingDecorator):
    def get_description(self) -> str:
        return self.pizza.get_description() + ", Cheese"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 1.0

class Olives(ToppingDecorator):
    def get_description(self) -> str:
        return self.pizza.get_description() + ", Olives"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 0.5

class Mushrooms(ToppingDecorator):
    def get_description(self) -> str:
        return self.pizza.get_description() + ", Mushrooms"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 0.7

# Abstract Base Payment Class (Interface)
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

# Concrete Payment Strategies
class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount:.2f} using PayPal")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount:.2f} using Credit Card")



def main():
    inventory_manager = InventoryManager()
    print("Welcome to the Pizza Restaurant!")

    while True:
        print("\nChoose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => to exit")
        pizza_choice = input("Enter the number of your choice: ")

        if pizza_choice == '0':
            break

        # Check and create base pizza
        if pizza_choice == "1" and inventory_manager.check_and_decrement("Margherita"):
            pizza = Margherita()
        elif pizza_choice == "2" and inventory_manager.check_and_decrement("Pepperoni"):
            pizza = Pepperoni()
        else:
            print("Pizza unavailable or out of stock!")
            continue

        # Add toppings
        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")

            if topping_choice == "1" and inventory_manager.check_and_decrement("Cheese"):
                pizza = Cheese(pizza)
            elif topping_choice == "2" and inventory_manager.check_and_decrement("Olives"):
                pizza = Olives(pizza)
            elif topping_choice == "3" and inventory_manager.check_and_decrement("Mushrooms"):
                pizza = Mushrooms(pizza)
            elif topping_choice == "4":
                break
            else:
                print("Topping unavailable or out of stock!")

        # Display final pizza details
        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        # Show final inventory
        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())
        # Payment Process
        print("\nChoose Payment Method:")
        print("1. PayPal")
        print("2. Credit Card")
        payment_choice = input("Enter the number of your choice: ")

        if payment_choice == "1":
            payment_method = PayPalPayment()
        elif payment_choice == "2":
            payment_method = CreditCardPayment()
        else:
            print("Invalid payment method. Defaulting to PayPal.")
            payment_method = PayPalPayment()

        payment_method.pay(pizza.get_cost())
        print("Order successful! Enjoy your pizza!")
