from NLP_preprocessing import preprocess
from semantic_retriever import semantic_search
from load_data import COFFEE_MENU, get_cheapest, get_expensive
import difflib

FAVOURITES = ["cappuccino", "latte", "cold brew"]

def hybrid_response(user_input: str) -> str:
    text = preprocess(user_input)

    if not text:
        return "Please ask about our coffee menu or prices ☕"

    # -------------------------------
    # 1️⃣ FAVOURITE / RECOMMENDATION
    # -------------------------------
    if "favourite" in text or "favorite" in text or "best" in text:
        favs = ", ".join([c.capitalize() for c in FAVOURITES])
        return f"Our customer favourites are {favs} ☕"

    # -------------------------------
    # 2️⃣ CATEGORY QUERIES
    # -------------------------------
    if "milk" in text:
        milk_coffees = [
            c.capitalize()
            for c, v in COFFEE_MENU.items()
            if v["category"] == "milk"
        ]
        return f"Milk coffees available are: {', '.join(milk_coffees)}"

    if "cold" in text:
        cold_coffees = [
            c.capitalize()
            for c, v in COFFEE_MENU.items()
            if v["category"] == "cold"
        ]
        return f"Cold coffees available are: {', '.join(cold_coffees)}"

    # -------------------------------
    # 3️⃣ CHEAPEST / EXPENSIVE
    # -------------------------------
    if "cheap" in text or "lowest" in text:
        c = get_cheapest()
        return f"The cheapest coffee is {c.capitalize()} at ₹{COFFEE_MENU[c]['price']}"

    if "expensive" in text or "costly" in text:
        c = get_expensive()
        return f"The most expensive coffee is {c.capitalize()} at ₹{COFFEE_MENU[c]['price']}"

    # -------------------------------
    # 4️⃣ EXACT / FUZZY COFFEE NAME
    # -------------------------------
    for coffee in COFFEE_MENU.keys():
        if coffee in text:
            return f"{coffee.capitalize()} costs ₹{COFFEE_MENU[coffee]['price']}"

    # -------------------------------
    # 5️⃣ SEMANTIC SEARCH
    # -------------------------------
    semantic = semantic_search(text)
    if semantic:
        return semantic

    # -------------------------------
    # 6️⃣ SAFE FALLBACK
    # -------------------------------
    return "I can help with coffee menu, prices, and recommendations ☕"
