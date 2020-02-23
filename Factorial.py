### iterating
##n = 5
##a = 1
##
##
##for b in range (1,n+1):
##    a = a * b
##    print(a)
##


# recursion
def fact(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n*fact(n-1)




print(fact(6))
    
