import math
input= int(input('enter number:'))
def  is_square():
    """ This is a function to find perfect square """
    
    a1= int(math.pow(input,0.5)) 
    a2=int(a1) * int(a1)
    print('nearest perfect square',(a2))


print is_square()
