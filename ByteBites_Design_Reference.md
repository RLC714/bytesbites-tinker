# ByteBites Design Reference

## Behavioral Instructions
- Model exactly four classes: Customer, FoodItem, Menu, Order. Do not add any others.
- Use composition, not inheritance. Category is a string attribute, not a subclass.
- Only include attributes and methods stated in the feature request.
  - Customer: name, purchase_history
  - FoodItem: name, price, category, popularity_rating
  - Menu: items; filter by category, sort by popularity
  - Order: items; calculate total
- Do not add payments, login, authentication, databases, or recommendation features.
- Keep code simple: plain Python classes, lists, and standard library only.
- Prefer small, readable methods with a one-line docstring.
- Do not over-engineer. If something is not in the spec, leave it out.
- Output UML as a Mermaid classDiagram.
