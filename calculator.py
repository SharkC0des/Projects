def main():
    
    # Ask about global variables. Put "global num1, num2, operator_choice" here didn't work.
    # How would I create a unit test for this????
    num1, num2, operator_choice = input_num()
    result = calculations(num1, operator_choice, num2)
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

        

        """

        --------- THE WTF IS GOING ON CODE----------- ASK DURING MEETING 
        Tried to re-prompt user when specified operator was not used: FAILEF
        Elif's are broken and I don't understand why
        """

        # Tried using "or" to include operators in one line didn't work. ASK "-" or "*" or "/"
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
def calculations(num1, operator_choice, num2,):
    add = num1  + num2
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

if __name__ == "__main__":
    main()