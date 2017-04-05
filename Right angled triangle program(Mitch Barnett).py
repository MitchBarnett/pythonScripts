def getinputs():
    """
    Gets the users inputs for the three sides of the triangle
    """
    a = float(input('Enter the first side length of your triangle: '))
    b = float(input('Enter the second side length of your triangle: '))
    c = float(input('Enter the final side length of your triangle: '))
    return [a, b, c]


def check(length):
    """
    This function will add to of the squared length and check
    if they add up to the other squared if it is true then the
    triangle will be right angled
    """
    if length[0] ** 2 + length[1] ** 2 == length[2] ** 2:
        return('This is a right angle triangle')

    elif length[1] ** 2 + length[2] ** 2 == length[0] ** 2:
        return('This is a right angle triangle')

    elif length[0] ** 2 + length[2] ** 2 == length[1] ** 2:
        return('This is a right angle triangle')

    else:
        return('This is not a right angle triangle')

#This is the code that will run
print (check(getinputs()))
input()
