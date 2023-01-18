

def add(a,b):
    answer = a+b
    print(str(a) + " + " + str(b) + "=" + str(answer) )

def sub(a,b):
    answer = a-b
    print(str(a) + " - " + str(b) + "=" + str(answer ))

def divide(a,b):
    answer = a/b
    print(str(a) + " / " + str(b) + "=" + str(answer) )

def multiply(a,b):
    answer = a*b
    print(str(a) + " * " + str(b) + "=" + str(answer) )


print("A.Addition")
print("B.Subtraction")
print("C.D.Division")
print("D.Multiplication")
print("D.Exit")

choice = input("input your choice: ")
if choice == "a" or choice =="A":
    print("Addition")
    a = int(input("input first number : "))
    b= int(input("input second number :  "))
    add(a,b)

elif choice =="b" or choice =="B":
    print("subtract")
    a = int(input("input first number"))
    b = int(input("input second number"))
    sub(a,b)



elif choice == "c" or choice == "C":
    print("Divide")
    a = int(input("input first number"))
    b = int(input("input second number"))
    divide(a,b)


elif choice == "d" or choice == "D":
    print("Multiplication")
    a = int(input("input first number"))
    b = int(input("input second number"))
    multiply(a,b)

elif choice == "e" or choice =="E":
    print("Exit")