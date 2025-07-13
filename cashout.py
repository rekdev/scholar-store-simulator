def payment_module(producto, cantidad, products):
    """
    Calculates the total cost of selected products and simulates a payment with change.

    Args:
        producto (list): List of selected product codes.
        cantidad (list): List of quantities corresponding to each selected product.
        products (dict): Dictionary of available products with prices.

    Returns:
        float: The amount paid.
        float: The change returned.
        float: The total cost.
    """
    total = 0

    print("\n--- Payment Module ---")
    for i in range(len(producto)):
        code = producto[i]
        qty = cantidad[i]
        price = products[code]["price"]
        subtotal = qty * price
        total += subtotal
        print(f"{products[code]['name']} x{qty} = ${subtotal:.2f}")

    print(f"\nTotal to pay: ${total:.2f}")

    while True:
        try:
            payment = float(input("Enter the amount paid: $"))
            if payment < total:
                print("Insufficient amount. Please enter a value equal or greater than the total.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    change = payment - total
    print(f"Change: ${change:.2f}")

    return payment, change, total
