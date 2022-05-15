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
    # Print list of appetizers
    print("Appetizers")
    print("-"*10)
    for key, value in app_names.items():
        print(key)

    entree_names = {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0, 'A Literal '
        'Garden': 0}
    # Print list of entrees
    print()
    print("Entrees")
    print("-"*7)
    for key, value in entree_names.items():
        print(key)

    dessert_names = {'Ice Cream': 0, 'Cake': 0, 'Pie': 0}
    # Print list of dessert
    print()
    print("Desserts")
    print("-"*8)
    for key, value in dessert_names.items():
        print(key)

    drink_names = {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}
    # Print list of drinks
    print()
    print("Drinks")
    print("-"*6)
    for key, value in drink_names.items():
        print(key)

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
            app_names[order_food] += 1
            if app_names.get(order_food) == 1:
                print()
                print("** " + str(app_names.get(order_food)) + " order of " +
                      order_food + " have been added to your meal **")
                print()
            elif app_names.get(order_food) > 1:
                print()
                print("** " + str(app_names.get(order_food)) + " orders of "
                      + order_food + " have been added to your meal **")
                print()
        elif order_food in entree_names:
            entree_names[order_food] += 1
            if entree_names.get(order_food) == 1:
                print()
                print("** " + str(entree_names.get(order_food)) + " order of "
                    "" + order_food + " have been added to your meal **")
                print()
            elif entree_names.get(order_food) > 1:
                print()
                print("** " + str(entree_names.get(
                    order_food)) + " orders of " + order_food + " have been "
                    "added to your meal **")
                print()
        elif order_food in dessert_names:
            dessert_names[order_food] += 1
            if dessert_names.get(order_food) == 1:
                print()
                print("** " + str(dessert_names.get(
                    order_food)) + " order of " + order_food + " have been "
                    "added to your meal **")
                print()
            elif dessert_names.get(order_food) > 1:
                print()
                print("** " + str(dessert_names.get(
                    order_food)) + " orders of " + order_food + " have been "
                    "added to your meal **")
                print()
        elif order_food in drink_names:
            drink_names[order_food] += 1
            if drink_names.get(order_food) == 1:
                print()
                print("** " + str(drink_names.get(
                    order_food)) + " order of " + order_food + " have been "
                    "added to your meal **")
                print()
            elif drink_names.get(order_food) > 1:
                print()
                print("** " + str(drink_names.get(
                    order_food)) + " orders of " + order_food + " have been "
                    "added to your meal **")
                print()
        elif order_food == 'quit':
            exit()
        else:
            print()
            print("That item does not exist.")
            print()

blank_line()

intro()
blank_line()
menu()
