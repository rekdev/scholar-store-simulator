def simulate_payment(selection_list):
    """
    Calculates the total price, asks the user to input the payment amount,
    and displays the change or error if not enough money is provided.

    Args:
        selection_list (list): A list of dictionaries with product info and quantity.

    Returns:
        float: The total paid by the user (only if payment is successful).
    """
    total = 0

    print("\n--- Payment Summary ---")
    for item in selection_list:
        product = item["product"]
        quantity = item["quantity"]
        subtotal = product["price"] * quantity
        total += subtotal
        print(f"{quantity} x {product['name']} = ${subtotal:.2f}")

    print(f"\nTotal to pay: ${total:.2f}")

    while True:
        try:
            paid = float(input("Enter payment amount: $"))

            if paid < total:
                print("Insufficient payment. Please enter a valid amount.")
            else:
                change = paid - total
                print(f"Payment accepted. Change: ${change:.2f}")
                return paid
        except ValueError:
            print("Please enter a valid number.")
