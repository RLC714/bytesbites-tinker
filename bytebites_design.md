# ByteBites Design (Final UML)

```mermaid
classDiagram
    class Customer {
        +str name
        +list~Order~ purchase_history
        +is_verified() bool
    }
    class FoodItem {
        +str name
        +float price
        +str category
        +float popularity_rating
    }
    class Menu {
        +list~FoodItem~ items
        +add_item(item)
        +filter_by_category(category) list
        +sort_by_popularity() list
    }
    class Order {
        +list~FoodItem~ items
        +add_item(item)
        +calculate_total() float
    }
    Customer "1" o-- "*" Order : purchase_history
    Menu "1" o-- "*" FoodItem : contains
    Order "1" o-- "*" FoodItem : selected items
```

## One-sentence roles
- **Customer**: a user with a name and past orders; verified if they have purchase history.
- **FoodItem**: one sellable item with name, price, category, popularity rating.
- **Menu**: the full collection of items, filterable by category and sortable by popularity.
- **Order**: a single transaction holding selected items and computing the total.
