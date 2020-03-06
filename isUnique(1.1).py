##word = ['a','e','b','e','c','g']
##         #e  b   e   c  g
##c=0
##a=1
##
##for i in range(c,len(word)):
##    #print("c= ",c,'\n')
##    c+=1
##    for j in range(a,len(word)):
##        #print("a=",a)
##        if (word[i] == word[j]):            
##            print("This string does not contain all unique characters")
##            break
##        else:
##            print("all unique", word[i], word[j])
##    a+=1




def checkUnique(n):
    a = [] # create emptp list 
    for i in n: 
        if i in a: #check to see if same element is in a. true true if it is
            return True
        else:
            a.append(i) # if not append the element from list to list a
    return False
    
b = ['c','a','1']

result = checkUnique(b)

if result:
    print("yes these characters are unique")
else:
    print("no they are not unique")
    
    


