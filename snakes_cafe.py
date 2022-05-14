# Create definitions for Opening Screen
def intro():
    print("*"*38)
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**")
    print("** To quit at any time, type 'quit' **")
    print("*"*38)

def blank_line():
    print(' \n ')

def menu():
    def appetizers():
        print("Appetizers")
        print("-"*10)
        print("Wings")
        print("Cookies")
        print("Spring Rolls")
    appetizers()

intro()
menu()