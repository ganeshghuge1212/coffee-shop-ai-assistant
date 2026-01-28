COFFEE_MENU = {
    "espresso": {"price": 80, "category": "espresso"},
    "americano": {"price": 100, "category": "espresso"},
    "ristretto": {"price": 90, "category": "espresso"},
    "lungo": {"price": 95, "category": "espresso"},
    "double espresso": {"price": 110, "category": "espresso"},

    "cappuccino": {"price": 120, "category": "milk"},
    "latte": {"price": 130, "category": "milk"},
    "flat white": {"price": 140, "category": "milk"},
    "macchiato": {"price": 110, "category": "milk"},
    "cortado": {"price": 125, "category": "milk"},
    "breve": {"price": 145, "category": "milk"},

    "mocha": {"price": 150, "category": "chocolate"},
    "white mocha": {"price": 160, "category": "chocolate"},
    "caramel latte": {"price": 155, "category": "flavored"},
    "vanilla latte": {"price": 150, "category": "flavored"},
    "hazelnut latte": {"price": 160, "category": "flavored"},

    "cold brew": {"price": 170, "category": "cold"},
    "iced latte": {"price": 150, "category": "cold"},
    "iced americano": {"price": 140, "category": "cold"},
    "frappe": {"price": 180, "category": "cold"},
    "nitro cold brew": {"price": 190, "category": "cold"},

    "affogato": {"price": 190, "category": "specialty"},
    "irish coffee": {"price": 200, "category": "specialty"},
    "turkish coffee": {"price": 170, "category": "specialty"},
    "vienna coffee": {"price": 165, "category": "specialty"},
    "dalgona coffee": {"price": 160, "category": "specialty"},

    "pour over": {"price": 140, "category": "filter"},
    "french press": {"price": 150, "category": "filter"},
    "aeropress": {"price": 155, "category": "filter"},
    "drip coffee": {"price": 120, "category": "filter"},
}

def get_cheapest():
    return min(COFFEE_MENU, key=lambda x: COFFEE_MENU[x]["price"])

def get_expensive():
    return max(COFFEE_MENU, key=lambda x: COFFEE_MENU[x]["price"])
