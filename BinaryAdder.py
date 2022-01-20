#aim: to return an interger representing the max number of consecutive zeros

import random

my_Array = []

def myArray(A1):
    x = random.randrange(50,101)
    for i in range (x):
        A1.append(random.randrange(0,2))
    return A1
    



def myfunction(A1):
    end = 0
    counter = 0
    for i in range (len(A1)):
        I1 = A1[i]
        if I1 ==0:
            counter += 1
        else:
            if counter > end:
                end = counter
                counter = 0
            else:
                counter = 0
    return end


A2 = (myArray(my_Array))

print(A2, "\nnumber of consecutive 0s:  ", myfunction(A2))