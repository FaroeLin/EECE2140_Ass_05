def compute_operation(myNum1, myNum2, operator):

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
  