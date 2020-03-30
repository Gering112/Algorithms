
# input:  4,1,3,2
# output: 2,3,1,4

def reverseArray(a=[]):
    values = []
    for i in range(0,a):
        value = int(input("enter a number"))
        values.append(value)
    print(values)
    reverse = [str(b) for b in values[::-1]]
    print(" ".join(reverse))
    
 
##reverse = [str(i) for i in newArra[::-1]]
##print(" ".join(reverse))

#value = int(input("enter a number"))

reverseArray(4)



'''
hacker ranks way of solving this problem 


a = int(input("enter a value ").strip())

Arra = [int (i) for i in input().strip().split(' ')]
newArr = []
reverse = ''
for i in (Arra):
    newArr.append(i)

reverse = (str(i) for i in newArra[::-1])
print(' '.join(reverse))

'''
