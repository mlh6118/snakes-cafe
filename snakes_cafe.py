# Create definitions for Opening Screen
def intro():
    print("*"*38)
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**")
    print("** To quit at any time, type 'quit' **")
    print("*"*38)

def blank_line():
     print()

def menu():
    app_names = {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0}
    menu_options(app_names, "Appetizers")

    entree_names = {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0, 'A Literal '
        'Garden': 0}
    menu_options(entree_names, "Entrees")

    dessert_names = {'Ice Cream': 0, 'Cake': 0, 'Pie': 0}
    menu_options(dessert_names, "Desserts")

    drink_names = {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}
    menu_options(drink_names, "Drinks")

    def order_statement():
        print()
        print("*"*35)
        print("** What would you like to order? **")
        print("*"*35)

    order_statement()

    status = True

    while status:
        order_food = input("> ")
        if order_food in app_names:
            order_response(app_names, order_food)
        elif order_food in entree_names:
            order_response(entree_names, order_food)
        elif order_food in dessert_names:
            order_response(dessert_names, order_food)
        elif order_food in drink_names:
            order_response(drink_names, order_food)
        elif order_food == 'quit':
            exit()
        else:
            print()
            print("That item does not exist.")
            print()


def order_response(food_category, order_food):
    food_category[order_food] += 1
    if food_category.get(order_food) == 1:
        print()
        print("** " + str(food_category.get(order_food)) + " order of " +
              order_food + " have been added to your meal **")
        print()
    elif food_category.get(order_food) > 1:
        print()
        print("** " + str(food_category.get(order_food)) + " orders of "
              + order_food + " have been added to your meal **")
        print()


def menu_options(menu_category, category_header):
    print()
    print(category_header)
    print("-"*len(category_header))
    # for key, value in menu_category.items():
    for key in menu_category.keys(): #same as line above.
        print(key)


blank_line()

intro()
menu()

