"""ByteBites core models.

Classes:
- FoodItem: a sellable item (name, price, category, popularity_rating)
- Menu: collection of FoodItems; filter by category, sort by popularity
- Order: a transaction of selected FoodItems; calculates total
- Customer: a user with a name and purchase_history of Orders
"""


class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def __repr__(self):
        return f"FoodItem({self.name!r}, {self.price}, {self.category!r}, {self.popularity_rating})"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add a FoodItem to the menu."""
        self.items.append(item)

    def filter_by_category(self, category):
        """Return items whose category matches (case-insensitive)."""
        return [i for i in self.items if i.category.lower() == category.lower()]

    def sort_by_popularity(self):
        """Return items sorted by popularity, highest first."""
        return sorted(self.items, key=lambda i: i.popularity_rating, reverse=True)


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add a FoodItem to the order."""
        self.items.append(item)

    def calculate_total(self):
        """Return the total cost of all items (0 if empty)."""
        return sum(i.price for i in self.items)


class Customer:
    def __init__(self, name, purchase_history=None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []

    def is_verified(self):
        """A customer is verified if they have past purchases."""
        return len(self.purchase_history) > 0


if __name__ == "__main__":
    burger = FoodItem("Spicy Burger", 10.0, "Mains", 4.8)
    soda = FoodItem("Large Soda", 5.0, "Drinks", 4.2)
    cake = FoodItem("Chocolate Cake", 6.5, "Desserts", 4.9)

    menu = Menu()
    for item in (burger, soda, cake):
        menu.add_item(item)

    print("Drinks:", menu.filter_by_category("Drinks"))
    print("By popularity:", menu.sort_by_popularity())

    order = Order()
    order.add_item(burger)
    order.add_item(soda)
    print("Total:", order.calculate_total())

    customer = Customer("Alex", [order])
    print(customer.name, "verified:", customer.is_verified())
