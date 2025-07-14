from welcome_menu import show_welcome_menu
from product_menu import show_products_menu, products
from product_selection import selection_menu
from cashout import simulate_payment 
from summary import show_purchase_summary


student_name = show_welcome_menu()
show_products_menu()
selection = selection_menu(products)
simulate_payment(selection)
show_purchase_summary(student_name, selection)