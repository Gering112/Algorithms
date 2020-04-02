'''
Given a string, print the even number index separated with
space then print the odd number index.

for example:

input: hacker
       rank

output: hce akr
        rk an
'''


string=""
string_odd = ""
newArr = []
t = int(input("enter: "))
for i in range(0,t):
    w = str(input("enter string: "))
    newArr = [w]
    for i in newArr:
        for j in range(0,len(i)):
            if j % 2 == 0:
                string = string+i[j]
            else:
                string_odd = string_odd + i[j]
        print(string, string_odd)
    string = ''
    string_odd = '' ''
