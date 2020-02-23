def fib (a):

    # return 1 if input is 1
    if a == 1:
        return 1
    # return 2 if input is 1
    elif a == 2:
        return 1
    else:
        # recursion
        return fib(a-1)+fib(a-2)

        
print(fib(10))


##def fibonacci(n):
##    i = 0
##    a = 1
##
##    if n == 0:
##        return 0
##    elif n == 1:
##        return 1
##    else:
##        #iterate from 2 to n
##        for b in range (2,n):
##            c = i + a
##            i = a
##            a = c
##            print(a)
##        return a
##print(fibonacci(9))
##
