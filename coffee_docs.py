from load_data import COFFEE_MENU

def build_documents():
    docs = []
    for coffee, info in COFFEE_MENU.items():
        docs.append(
            f"{coffee.capitalize()} is a {info['category']} coffee. "
            f"It costs ₹{info['price']}."
        )
    return docs
