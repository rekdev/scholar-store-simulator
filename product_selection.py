def selection_menu(products: dict):
    """
    Show a product selection menu where you can choose a product and the quantity of it,
    and then returns a list with the selected products:

    Args:
        products (dict): A dictionary with the products' info. 

    Returns:
        list: A list with all the selected products composed by and array of both quantity and the product info.
    """
    selection_list = []

    while True:
        print("Select a product by number or press q to finish the sell.")
        selection = input(": ")

        if selection == "q":
            break
        elif selection in products.keys():
            selected_product = products[selection]
            quantity = int(input("How many do you want? "))

            if quantity < 1:
                print("! > You have selected a non-valid quantity.")
                continue

            selection_list.append({
                "quantity": quantity,
                "product": selected_product
            })

            print(
                f"You have just selected: {quantity}: {selected_product['name']}")

        else:
            print("You selected an invalid option.")

    return selection_list
