print("\n****************************Python Calculator****************************")
print("*****************************-by BritoFelipe*****************************")

def sum (n1, n2):
    return n1 + n2
def subtract (n1, n2):
    return n1 - n2
def multiply (n1, n2):
    return n1 * n2
def divide (n1, n2):
    return n1 / n2

option = 1

while option != 0:
    print("\nPlease select one option")
    print("1 - Sum")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")
    option = int(input())

    if (option >= 1) and (option <= 4):
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
    elif option != 0:
        print("Please select a valid option")

    if option == 1:
        print(num1, " + ", num2, " = ", sum(num1, num2))
    elif option == 2:
        print(num1, " - ", num2, " = ", subtract(num1, num2))
    elif option == 3:
        print(num1, " x ", num2, " = ", multiply(num1, num2))
    elif option == 4:
        if num2 == 0:
            print("You can't divide by zero")
        else:
            print(num1, " / ", num2, " = ", divide(num1, num2))


    input("\nPress enter to continue")





