# Draft from AI (no reference file)

First-pass diagram from plain chat, before adding the reference file. Note the extra classes and inheritance not in the spec.

```mermaid
classDiagram
    class User {
        +int id
        +str email
        +str password
        +login()
    }
    class Customer {
        +str name
        +list purchase_history
        +verify_user()
    }
    class FoodItem {
        +str name
        +float price
        +str category
        +float popularity_rating
    }
    class Dessert
    class Drink
    class Menu {
        +list items
        +filter_by_category()
        +recommend_items()
    }
    class Order {
        +list items
        +str status
        +calculate_total()
        +process_payment()
    }
    class PaymentProcessor {
        +charge()
    }
    User <|-- Customer
    FoodItem <|-- Dessert
    FoodItem <|-- Drink
    Menu o-- FoodItem
    Order o-- FoodItem
    Customer --> Order
    Order --> PaymentProcessor
```

## Problems
- Adds classes not in the spec (User, Dessert, Drink, PaymentProcessor).
- Uses inheritance where simple attributes work (category is just a string).
- Adds features not requested (login, recommend_items, process_payment, status).
