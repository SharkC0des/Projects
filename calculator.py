def main():
    # Ask about global variables. Put "global num1, num2, operator_choice" here didn't work.
    # How would I create a unit test for this????
    input_num()
    Calculations()

def input_num():
    global num1, num2, operator_choice
# Prompts user for first number
    while True:
        try:
             num1 = int(input("First Number: ")) #ASK ABOUT ADDING FLOATS; Tried int,float(input), error occurs
        except ValueError:
                print("Please, type in a number. ")
        else:
         break

# Prompt user for Operator

    while True: #ASK ABOUT WHAT EXCEPTION WOULD WORK HERE
        operator_choice = input("Choose Operator:(+, -, *, /) ") 
        break

# Prompts for second number
        
    while True:    
        try:
            num2 = int(input("Second Number: "))
        except ValueError:
                print("Please, type in a number. ")
        else:
            break

# Addition
def Calculations():
    add = num1  + num2
    #Subtraction
    subtract = num1 - num2
    #Multiplication
    multiply = num1  * num2
    #Divison
    divide = num1  / num2

    #Calculating Addition
    if operator_choice == "+":
        print(add)

    # Calculating Subtraction
    elif operator_choice == "-":
        print(subtract)

    # Calculating Multiplication
    elif operator_choice == "*":
        print(multiply)

    # Calculating Division
    elif operator_choice == "/":
        print(divide)

    # User's Fault, I take no responsibility
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()