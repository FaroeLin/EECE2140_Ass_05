def factorialNumber(myNum):
    result = 1      #Handles the case when the input is 0, since the factorial of 0 is 1
    for index in range(1, myNum + 1):       #Loop covers all the integers need to multiply together
        result *= index     #Multiply the current value of result by the current value of index, completing the factorial calculation
    
    return result