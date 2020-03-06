##string = "abcdefghijklmnopqrstuvwxyz"
##reverse = ""
##
##
##for i in range(0,len(string)):
##    reverse = str(string[i]) + reverse
##print(reverse)
##                  




def reverse(str):
    reverse = ""
    if len(str) == 0:
        return ""
    else:
        for i in str:
            reverse = i+reverse
        return reverse
            
print(reverse("gering"))
