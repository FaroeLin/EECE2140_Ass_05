def calculateHypotenuse(base, perpendicular):
    def calculateSquare(myNum):     #Function that calculate the square of a number
        return myNum ** 2
    
    return (calculateSquare(base) + calculateSquare(perpendicular)) ** 0.5      #Calculation of the hypotenuse base on the formula given
