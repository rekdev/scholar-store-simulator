products = {
    "1": {"name": "Strawberry Shake", "price": 20, },
    "2": {"name": "Halls", "price": 10, },
    "3": {"name": "Fruts Cookies", "price": 20, },
    "4": {"name": "Takis", "price": 15, },
    "5": {"name": "Club Sandwich", "price": 42, },
    "6": {"name": "Dr Pepper", "price": 18, },
    "7": {"name": "Coffee", "price": 15, },
    "8": {"name": "Chai Tea", "price": 30, },
    "9": {"name": "Oreo Milkshake", "price": 60, },
    "10": {"name": "Coconut Water", "price": 20, },
}


def show_products_menu():
    """
    This function displays the product menu with their respective prices.
    """
    print("\n--- Product Menu ---")
    for code, data in products.items():
        name = data["name"]
        price = data["price"]

        print(f"{code}. {name} - ${price: .2f}")
