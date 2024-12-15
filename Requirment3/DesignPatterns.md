# **Design Patterns in Pizza Ordering System**

## **1. Decorator Pattern**

### **Purpose**
It is used to extend the functionality of objects without modifying the main objects' class.

### **Application in the Pizza Ordering System**
The pizza system uses the **Decorator Pattern** to add toppings like **Cheese**, **Olives**, and **Mushrooms** dynamically to the base pizzas (**Margherita** and **Pepperoni**). Each topping enhances the description and cost of the pizza without changing the pizza base class.

### **Advantages**
- Adheres to the **Open-Closed Principle**: New toppings can be added without modifying existing code.
- Extensible and Maintainable: Easy to add new toppings dynamically.

### **Code Implementation**
```python
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
```



---

## **2. Strategy Pattern**

### **Purpose**
It allows selecting an appropriate strategy based on user choice.

### **Application in the Pizza Ordering System**
The payment methods (e.g., PayPal and Credit Card) are implemented using the **Strategy Pattern**. Each payment method is treated as a separate strategy.

### **Advantages**
- Adheres to the **Open-Closed Principle**: New payment methods can be added without modifying existing code.
- Separates payment logic from the main system, enhancing maintainability.

### **Code Implementation**
```python

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
```


---

## **3. Singleton Pattern**

### **Purpose**
The ensures that a class has only one instance and provides a global access to it.

### **Application in the Pizza Ordering System**
The **Inventory Manager** is implemented as a **Singleton** to ensure that there is a single source for the pizzas and toppings.

### **Advantages**
- Ensures a single instance of the inventory manager.
- Provides global access to the inventory.
- Prevents multiple instances that could lead to inconsistent states.

### **Code Implementation**

```python
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
    
```


---

## **Overengineering**

### **Definition**
Overengineering occurs when a system is made unnecessarily complex by implementing features that are not required for solving the current problem. 

### **Example of Overengineering in the Pizza Ordering System**
Suppose we add **10+ payment methods** (e.g., Bitcoin, Venmo, Google Pay, etc.) before knowing if the restaurant requires them.

### **Why is This Overengineering?**
1. **Unnecessary Features**: Adding payment methods that are not required.
2. **Wasted Time**: Implementing features that may never be used.

### **How to Avoid Overengineering**
1. **Start Simple**: Implement only the essential features first.
2. **Add features Gradually**: Add new features based on user requirements.
3. **YAGNI Principle**: "You Aren't Gonna Need It"—avoid adding functionality unless it is absolutely necessary.

**Balanced Example in pizza system**:
```python
# Concrete Payment Strategies
class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount:.2f} using PayPal")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount:.2f} using Credit Card")
```

---

## **Conclusion**
The use of **Decorator Pattern**, **Strategy Pattern**, and **Singleton Pattern** ensures flexibility, maintainability, and extensibility in the pizza ordering system. Avoiding overengineering keeps the code simple, efficient, and aligned with current requirements.
