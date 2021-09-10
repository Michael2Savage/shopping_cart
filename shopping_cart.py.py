# Excersize 1 / Shopping cart

killswitch = True

cart = []
print("Welcome to your interactive cart! Type 'quit' at any point to quit.")

command = input("Please type the command you wish to execute, Show/Add/Delete/Clear or Quit.")

while killswitch == True:
    if command.lower() == "show":
        print(f"Your cart: {cart}")
        command = input("What would you like to do next?")

    elif command.lower() == "add":
        new_item = input("What would you like to add?")
        if new_item.lower() in cart:
            print("That's already in your cart.")
        elif new_item.lower() not in cart:
            cart.append(new_item)
            print(f"You added: {new_item}")
        command = input("What would you like to do next?")

    elif command.lower() == "delete":
        if cart == False:
            print("Your cart is empty")
            command = input("What would you like to do next?")
        print(f"Here's what's in your cart: {cart}")
        del_item = input("What do you want to delete?").lower()
        cart.remove(del_item)
        command = input("What would you like to do next?")

    elif command.lower() == "clear":
        last_chance = input("Are you sure you want to clear your cart? <yes/no>")
        if last_chance.lower() == "yes":
            cart.clear()
            print("Your cart has been cleared!")
            command = input("What would you like to do next?")
        elif last_chance.lower() == "no":
            command = input("What would you like to do next?")
        else:
            last_chance = "no"

    elif command.lower() == "quit":
        print(f"Your cart: {cart}")
        killswitch = False

    else:
        print("Are you stupid or just ugly? use one of the commands lol")
        command = input("What would you like to do next?")

