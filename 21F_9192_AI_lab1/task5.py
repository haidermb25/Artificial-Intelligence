

#Task:5

#Function for add numbers
def add_number(a, b):
    return a + b

# Function for subtract numbers
def subtract_number(a, b):
    return a - b

# Function for take square
def square_number(a, b):
    return a**2, b**2

# Function for take cube
def cube_number(a, b):
    return a**3, b**3

def calculator():
    value1 = int(input("Enter the first number: "))
    value2 = int(input("Enter the second number: "))

    print("\nPress +: for add 2 numbers")
    print("Press -: for subtract 2 numbers")
    print("Press *: for take square of both numbers")
    print("Press **: for take cube of both numbers\n ")
    choice = input("Enter the choice: ")

    if choice == '+':
        print("Addition Result is:", add_number(value1, value2))
    elif choice == '-':
        print("Subtraction Result is:", subtract_number(value1, value2))
    elif choice == '*':
        r1, r2 = square_number(value1, value2)
        print("Square of num1 is: %d  Square of num2 is: %d" % (r1, r2))
    elif choice == '**':
        r1, r2 = cube_number(value1, value2)
        print("Cube of num1 is: %d  Cube of num2 is: %d" % (r1, r2))
    else:
        print("Enter Wrong Input!!")

if __name__ == "__main__":
    calculator()
