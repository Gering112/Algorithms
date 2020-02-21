def fib (a):

    # return 0 if input is 0
    if a == 0:
        return 0
    # return 1 if input is 1
    elif a == 1:
        return 1
    else:
        return fib(a-1)+fib(a-2)

        
print(fib(20))


##i = 1
##a = 0
##n=0
##
##while n < 12:
##    n = i + a
##    i = a
##    a = n
##    print (n)
