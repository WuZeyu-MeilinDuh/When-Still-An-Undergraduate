
import pprint

food_kg = {"Justin": {"sausage": 1, "broccoli": 0.6, "carrot": 1},
         "Susanna": {"beef": 0.8, "cheese": 0.6, "broccoli": 0.5},
         "Douglas": {"sausage": 0.7, "beef": 0.5, "cheese": 0.6, "carrot": 0.3, "wine": 1.2},
         "Henry": {"chicken": 0.4, "beef": 0.4, "cheese": 1, "wine": 0.6}}

inventory = {}
for g, f in food_kg.items():
    for food, weight in f.items():
        inventory.setdefault(food, 0)
        inventory[food] = inventory[food] + weight
pprint.pprint(inventory)