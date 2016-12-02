def factorial(number):#Finds the factorial of the number
    """This functions finds the trailing zeros of a specific number"""
    if number == 0:
        return 1
    else:
        
        return number * factorial(number-1)
def countTrailingzeros(number): #calculates the trailing zeros of the specific number,taking away the length of the string without removing the zeros,give the number of zeros.
        f = factorial(number)
        strF = str(f)
        return len(strF) -len(strF.rstrip('0'))

print(countTrailingzeros(5,))
print(countTrailingzeros(10))
print(countTrailingzeros(15))
print(countTrailingzeros(25))
print(countTrailingzeros(35))
