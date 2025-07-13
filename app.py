from welcome_menu import show_welcome_menu
from product_menu import show_products_menu, products
from product_selection import selection_menu

student_name = show_welcome_menu()
show_products_menu()
selection = selection_menu(products)
