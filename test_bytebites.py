from models import FoodItem, Menu, Order, Customer


def make_menu():
    menu = Menu()
    menu.add_item(FoodItem("Spicy Burger", 10.0, "Mains", 4.8))
    menu.add_item(FoodItem("Large Soda", 5.0, "Drinks", 4.2))
    menu.add_item(FoodItem("Chocolate Cake", 6.5, "Desserts", 4.9))
    menu.add_item(FoodItem("Iced Tea", 3.0, "Drinks", 3.9))
    return menu


def test_calculate_total_with_multiple_items():
    order = Order()
    order.add_item(FoodItem("Spicy Burger", 10.0, "Mains", 4.8))
    order.add_item(FoodItem("Large Soda", 5.0, "Drinks", 4.2))
    assert order.calculate_total() == 15.0


def test_order_total_is_zero_when_empty():
    assert Order().calculate_total() == 0


def test_filter_by_category_returns_only_matching_items():
    drinks = make_menu().filter_by_category("Drinks")
    assert len(drinks) == 2
    assert all(i.category == "Drinks" for i in drinks)


def test_filter_by_unknown_category_returns_empty_list():
    assert make_menu().filter_by_category("Soup") == []


def test_sort_by_popularity_highest_first():
    ratings = [i.popularity_rating for i in make_menu().sort_by_popularity()]
    assert ratings == sorted(ratings, reverse=True)


def test_customer_with_history_is_verified():
    assert Customer("Alex", [Order()]).is_verified()
    assert not Customer("Sam").is_verified()
