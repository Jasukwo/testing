import time

mylist = ["notebook", "pen", "calculator", "textbook", "ruler", "phone", "laptop", "money", "shoe"]

def remove():
    a = []
    print(mylist)
    while a not in mylist:
        a= input("ENTER ITEM TO BE REMOVED: ")
        if a in mylist:
            print("Removing Item, please wait...")
            time.sleep(3)
            mylist.remove(a)
            print("Item Removed Successfully!")
            print(mylist)
            quit()
        else:
           print("SORRY, YOUR ITEM IS NOT IN LIST, TRY AGAIN.")
           continue


def add_item():

    print(mylist)
    x = input("ENTER ITEM TO BE INSERTED: ")

    if x in mylist:
        y = input("ITEM ALREADY EXIST, ENTER A DIFFERENT ITEM, PRESS 1 TO QUIT: ")
        if y=="1":
            quit()
    else:
        try:
            p = int(input("ENTER INDEX POSITION TO INSERT: "))
            if p<len(mylist)+1:

                print("Inserting Item Please Wait...")
                time.sleep(3)
                mylist.insert(p, x)
                print("Item Inserted Successfully!")
                print(mylist)
            else:
                print("YOUR INDEX IS OUT OF RANGE. RESTART THE PROGRAM TO CONTINUE")
                quit()
        except ValueError:
            print("ValueError, RESTART THE PROGRAM")
            quit()
        except TypeError:
            print("TypeError, RESTART THE PROGRAM")
            quit()
def sorting():
    print(mylist)
    print("Sorting In Progress...")
    time.sleep(3)
    mylist.sort()
    print("List Sorted Successfully!!")
    print(mylist)

def reverselist():
    print(mylist)
    print("Reversing Your List...")
    time.sleep(3)
    mylist.reverse()
    print("List Reversed Successfully!!")
    print(mylist)

name = input("ENTER YOUR NAME TO START: ").upper()
print(f"\n WELCOME TO THIS PROGRAM {name}, SELECT FROM THE OPTIONS BELOW")
print("PRESS 1 TO VIEW LIST")
print("PRESS 2 TO INSERT TO LIST")
print("PRESS 3 TO REMOVE FROM LIST LIST")
print("PRESS 4 TO SORT THE LIST")
print("PRESS 5 TO REVERSE LIST")
print("PRESS Q TO QUIT LIST")

while True:
    start = input('ENTER AN OPTION: ')
    if start == "1":
        print(mylist)

        another = input("PRESS 2 TO INSERT TO LIST OR 9 TO SELECT ANOTHER OPTION: ")
        if another == "2":
            add_item()
            break
        elif another == "9":
            continue
        elif another == "q".lower():
            quit()
        else:
            print("YOU HAVE ENTERED AN INVALID OPTION, TRY AGAIN!!")
            continue

    elif start == "2":
        add_item()
        break

    elif start == "3":
        remove()

    elif start == "4":
        sorting()
        break
    elif start == "5":
        reverselist()

    elif start == "q".lower():
        print("Closing Program...")
        time.sleep(3)
        print("Bye, See You Next Time")
        quit()

    else:
        print("YOU HAVE ENTERED AN INVALID OPTION, PLEASE TRY AGAIN!!")
        continue



