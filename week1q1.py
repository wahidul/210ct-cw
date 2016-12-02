import random
x = [1,2,3,4,5,6]

for i in range(0,6):
    
    y = random.randint(0,5)
    print i
    print "Randmb bit " + str(y)
    temp = x[i]
    print "Temp is {}".format(temp)
    x[i] = x[y]
    x[y] = x[i]
    x[y] = temp

    print "x is now {0}".format(x)
    
    

    #Swap items at x[i] and x[y]

print x 
