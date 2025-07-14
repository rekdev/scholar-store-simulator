def show_purchase_summary(student_name: str, selection_list: list):
    """
    Displays a detailed summary of the purchase, including each item, quantity,
    individual price, subtotal, and the grand total.

    Args:
        student_name (str): The name of the student (client).
        selection_list (list): A list of dictionaries with product info and quantity.
    """
    total_purchase = 0
    print("\n--- Purchase Summary ---")
    print(f"Client: {student_name}\n")
    print(f"{'Product':<20} {'Qty':<5} {'Price':<10} {'Subtotal':<10}")
    print("-" * 55)

    for item in selection_list:
        product = item["product"]
        quantity = item["quantity"]
        subtotal = product["price"] * quantity
        total_purchase += subtotal
        print(
            f"{product['name']:<20} {quantity:<5} ${product['price']:.2f}    ${subtotal:.2f}")

    print("-" * 55)
    print(f"{'Total:':<37} ${total_purchase:.2f}")
    print("------------------------")
