import sys

class  BasicMathOperations():
    def greetUser(self):
        while 1:
            firstName = input("Enter your first name: ")        #Get user's name
            lastName = input("Enter your last name: ")
            if not firstName.strip() or not lastName.strip():       #If user do not enter the full name
                print(">>First name and/or last name cannot be empty. Try again<<")
            else:
                break
        
        fullName = firstName + " " + lastName       #Spell the fullname
        greeting = f"Hello, {fullName}! How are you today?"     #Print the fullname with greeting

        return greeting

    def addNumbers(self):
        while 1:
            try:
                myNum1 = float(input("Enter the first number here: "))      #Get the numbers
                myNum2 = float(input("Enter the second number here: "))
                
                return myNum1 + myNum2      #Calculate the sum and return
            except ValueError:      #If not able to process calculation
                print(">>One of your input is not number. Try again<<")
    
    def computeOperation(self):
        while 1:
            try:
                myNum1 = float(input("Enter the first number here: "))      #Get the numbers and operator
                myNum2 = float(input("Enter the second number here: "))
                operator = input("Enter the type of opreation here: ")

                if operator == "+":     #If require addition
                    return myNum1 + myNum2
    
                elif operator == "-":       #If require subtraction
                    return myNum1 - myNum2
    
                elif operator == "*":       #If require multiplication
                    return myNum1 * myNum2
    
                elif operator == "/":       #If require division
                    if myNum2 != 0:     #If the divisor is not zero
                        return myNum1 / myNum2
                    else:
                        return "Division cannot be zero."
                
                else:
                    print(">>Invalid operation symbol. No matching results. Try again<<")
            except ValueError:      #If not able to process calculation
                print(">>One  of your input is not number. Try again<<")

    def squareNumber(self):
        while 1:
            try:
                myNum = float(input("Enter the number here: "))     #Get the number
                return myNum ** 2       #Return its square
            except ValueError:      #If not able to process calculation
                print(">>One of your input is not number. Try again<<")

    def factorialNumber(self):
        while 1:
            try:
                myNum = int(input("Enter the number here: "))     #Get the number
                result = 1      #Handles the case when the input is 0, since the factorial of 0 is 1
                for index in range(1, myNum + 1):       #Loop covers all the integers need to multiply together
                    result *= index     #Multiply the current value of result by the current value of index, completing the factorial calculation
    
                return result
            except ValueError:      #If not able to process calculation
                print(">>One of your input is not number. Try again<<")
    
    def displayCount(self):
        while 1:
            try:
                start = int(input("Enter the first number here: "))     #Get the range
                end = int(input("Enter the second number here: "))
                for number in range(start, end + 1):        #Adding 1 to ensures the end number is part of the sequence
                    print(number)       #Print each number
                    
                return 0
            except ValueError:      #If not able to process
                print(">>One of your input is not number. Try again<<")

    def calculateHypotenuse(self):
        def calculateSquare(myNum):     #Function that calculate the square of a number
            return myNum ** 2
        
        while 1:
            try:
                base = float(input("Enter the value of base here: "))       #Get the values
                perpendicular = float(input("Enter the value of perpendicular here: "))

                return (calculateSquare(base) + calculateSquare(perpendicular)) ** 0.5      #Calculation of the hypotenuse base on the formula given
            except ValueError:
                print(">>One of your input is not number. Try again<<")
    
    def calculateArea(self, width, height):

        return width * height
    
    def findPower(self):
        while 1:
            try:
                base = float(input("Enter the value of base here: "))        #Get the values
                exponent = float(input("Enter the value of exponent here: "))

                return base ** exponent     #Return the power of the given number
            except ValueError:      #If not able to process
                print(">>One of your input is not number. Try again<<")

    def getType(self):
        myArgument = input("Enter the argument here: ")
        try:
            processedMyArgument = eval(myArgument)      #Try to evaluate the input

            return type(processedMyArgument)        #Returns the type of the argument
        except:     #If not able to evaluate, which means that itself is a string type
            
            return type(myArgument)         #Returns the type of the argument


def main():
    ops = BasicMathOperations()     #Instance of BasicMathOperations
    
    print("--Welcome to this simulation program--")
    print(">>Function List<<")
    print("-----------------------------")
    print("1 Greeting user")
    print("2 Addition")
    print("3 Specify mathematical operations")
    print("4 Square number")
    print("5 Factorial number")
    print("6 Counting display")
    print("7 Calculate hypotenuse")
    print("8 Calculate area")
    print("9 Find number's power")
    print("10 Get type of argument")
    print("e Exit the program")
    print("-----------------------------")

    while 1:
        choice = input(">>Please select the function you want to use<<")        #Prompt user to choose

        if choice == '1':       #Call the specified function based on the user's selection
            print(ops.greetUser())
            print(">>Request execute successfully<<")       #Prompts the user that the function call is successful

        elif choice == '2':
            print(ops.addNumbers())
            print(">>Request execute successfully<<")
        
        elif choice == '3':
            print(ops.computeOperation())
            print(">>Request execute successfully<<")
        
        elif choice == '4':
            print(ops.squareNumber())
            print(">>Request execute successfully<<")

        elif choice == '5':
            print(ops.factorialNumber())
            print(">>Request execute successfully<<")

        elif choice == '6':
            ops.displayCount()
            print(">>Request execute successfully<<")

        elif choice == '7':
            print(ops.calculateHypotenuse())
            print(">>Request execute successfully<<")
        
        elif choice == '8':
            while 1:
                try:
                    myWidth = input("Enter the value of width here: ")      #Get the values
                    myHeight = input("Enter the value of height here: ")
                    testNum = float(myWidth + myHeight)     #Check if the user input is a valid number, works with line 158
            
                    print("Pass as values: ")       #Call the function by passing with values
                    print(ops.calculateArea(float(myWidth), float(myHeight)))

                    print("Pass as variables: ")        #Call the function by passing with variables
                    width = float(myWidth)      #Conver to float type
                    height = float(myHeight)
                    print(ops.calculateArea(width, height))

                    print(">>Request execute successfully<<")

                    break
                except ValueError:      #If not able to process
                    print(">>One or two of your input is not number. Try again<<")
        
        elif choice == '9':
            print(ops.findPower())
            print(">>Request execute successfully<<")

        elif choice == '10':
            print(ops.getType())
            print(">>Request execute successfully<<")
        
        elif choice == 'e':
            print(">>Exit successfully<<")
            sys.exit(0)
        
        else:       #If it is an invalid input
            print(">>Invalid selection. Try again<<")

main()