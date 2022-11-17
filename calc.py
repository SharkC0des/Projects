import sys
def main():
    
    # Ask about global variables. Put "global num1, num2, operator_choice" here didn't work.
    # How would I create a unit test for this????
    num1, num2, operator_choice = input_num()
    result = [addition, subtraction ,multiplication, divison(num1, operator_choice, num2)] #Moified
    print(result)
        


def input_num():
# Prompts user for first number
    while True:
        try:
             num1 = float(input("First Number: ")) #ASK ABOUT ADDING FLOATS; Tried int,float(input), error occurs
        except ValueError:
                print("Please, type in a number. ")
        else:
         break

# Prompt user for Operator
    while True: #ASK ABOUT WHAT EXCEPTION WOULD WORK HERE
        operator_choice = input("Choose Operator:(+, -, *, /) ") 
        if not operator_choice in ["+", "-", "*", "/"]:
            print("Choose an operator from the list provided")
        else:
            break
# Prompts for second number   
    while True:    
        try:
            num2 = float(input("Second Number: "))
        except ValueError:
                print("Please, type in a number. ")
        else:
            break

    return num1, num2, operator_choice
# Addition
def addition(num1, operator_choice, num2):
    if operator_choice == "+":
        add = num1  + num2
    return add
#subtraction
def subtraction(num1, operator_choice, num2):
    if operator_choice == "-":
        subtract = num1 - num2
    return subtract
#multiplicaiton
def multiplication(num1, operator_choice, num2):
    if operator_choice == "-":
        multiply = num1 * num2
    return multiply
#Division
def divison(num1, operator_choice, num2):
    if operator_choice == "/":
        divide = num1 / num2
        try:
            divide = num1 / num2
        except ZeroDivisionError:
            print("Can't divide by Zero")
        else:
            sys.exit(1)
    return divide



    """
    #Subtraction
    subtract = num1 - num2
    #Multiplication
    multiply = num1  * num2
    #Divison
    divide = num1  / num2

    #Calculating Addition
    if operator_choice == "+":
        return num1 + num2

    # Calculating Subtraction
    elif operator_choice == "-":
        return num1 - num2

    # Calculating Multiplication
    elif operator_choice == "*":
        return num1 * num2

    # Calculating Division
    elif operator_choice == "/":
        return num1 / num2

    # User's Fault, I take no responsibility
    else:
        print("Invalid Input; Try Again")
"""
if __name__ == "__main__":
    main()
