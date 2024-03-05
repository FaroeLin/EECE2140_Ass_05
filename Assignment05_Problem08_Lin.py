def calculateArea(width, height):

    return width * height

#Passing arguments as values
area = calculateArea(5, 10)
print(str(area))

#Passing arguments as variables
myWidth = 5
myHeight = 10
myArea = calculateArea(myWidth, myHeight)
print(str(myArea))