import time
menu = {"rice":200, "beans":150, "pork":100, "akpu":200, "water":100, "coke":150, "fanta":150}
new_menu= {}



#function to print the food items
def food_items():
    for item, price in menu.items():
        print(item, "= ", "₦",price)

#this function adds a new food item and its price
def chef_add():
    menu = {"rice": 200, "beans": 150, "pork": 100, "akpu": 200}

    new_menu = {}

    while True:
        a = input("ENTER A FOOD ITEM TO BE ADDED: ").lower()
        if a == "Q":
            quit()

        elif a.isalpha():
            if a in menu or new_menu:
                print("ERROR: The food item you entered is already in your menu; Press Q to quit")
                continue

            b = input("ENTER THE PRICE OF THE FOOD ITEM: ")

            if b.isdigit():
                int(b)

                print("Processing...")
                time.sleep(5)
                new_menu=menu
                new_menu[a] = b
                print("The food item has been added to your Menu Successfully")
                for item, price in menu.items():
                    print(item, "= ", "₦",price)

                break
            else:
                print("ERROR: Please enter a valid price for the food item")
                continue
        else:
            print("ERROR: Enter a valid name for food item")

#this function removes a food item
def remove_item():
    while True:

        x = input("ENTER THE FOOD ITEM TO BE REMOVED: ").lower()

        if x.isalpha():

            if x in menu:
                del menu[x]
                print("Preparing to remove...")
                time.sleep(2)
                print("Removing...")
                time.sleep(5)
                print()
                print("Food Item Has Been Removed Successfully")

                for item, price in menu.items():
                    print(item, "= ", "₦",price)

                break

            else:
                print("SORRY THE ITEM IS NOT IN YOUR FOOD MENU, PLEASE TRY AGAIN")

                continue

        else:
            print("PLEASE ENTER A VALID NAME FOR FOOD ITEM")

            continue

#this function places an order
def order_item():
    print("BELOW ARE THE AVAILABLE FOOD ITEMS")

    for item, price in menu.items():
        print(item, "= ", "₦", price)
    total = 0
    lst = list(menu.keys())

    while True:
        choices = input("\nMAKE YOUR CHOICE, PRESS S TO SUBMIT: ").lower()

        if choices.isalpha():

            if choices in lst:
                total = total+menu[choices]

            elif choices == "s":
                print("Please wait, your order is being processed...")
                time.sleep(5)
                print("Submitting your order...")
                time.sleep(5)
                print("YOUR ORDER HAS BEEN SUBMITTED SUCCESSFULLY!")
                time.sleep(2)
                print(f"\nTOTAL AMOUNT FOR ORDER IS ₦ {total}")

                break

            else:
                print("SORRY, THE FOOD IITEM YOU ENTERED IS NOT IN OUR MENU, PLEASE MAKE ANOTHER CHOICE")
                continue
        else:
            print("PLEASE ENTER A VALID FOOD ITEM")
            continue


print("HELLO!! WELCOME TO JAMES RESTAURANT")

print("PLEASE SELECT FROM THE SERVICE")

print('''\nPRESS 1 TO VIEW FOOD ITEMS
PRESS 2 TO ADD FOOD ITEMS
PRESS 3 TO REMOVE FOOD ITEM
PRESS 4 TO PLACE AN ORDER
PRESS Q TO QUIT
''')
while True:
    start = input("ENTER FROM THE OPTIONS ABOVE:\n")
    if start == "1":
        food_items()
        o = input("PRESS 4 TO PLACE AN ORDER OR 9 TO SELECT ANOTHER OPTION AND Q TO QUIT: ")
        if o == "4":
            order_item()
            break
        elif o == "9":
            continue

        elif o == "Q".lower():
            print("GOOD BYE...")
            time.sleep(2)
            quit()
        else:
            print("ENTER A VALID OPTION")
            continue


    elif start == "2":
        chef_add()
        break

    elif start == "3":
        remove_item()
        break

    elif start == "4":
        order_item()
        break

    elif start == "Q".lower():
        print('''ITS NICE HAVING YOU, SEE YOU SOME OTHER TIME.
        BYE!!!''')
        quit()

    else:
        print("YOU HAVE ENTERED AN INVALID OPTION, TRY AGAIN.")
        continue








