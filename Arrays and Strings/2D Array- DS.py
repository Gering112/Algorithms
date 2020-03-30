"""
calculating hour glass sum in an array 
y - vertical
x - horizontal 
"""


arr = [
    [-9,-9,-9,1,1,1],
    [0,-9,0,4,3,2],
    [-9,-9,-9,1,2,3],
    [0,0,8,6,6,0],
    [0,0,0,-2,0,0],
    [0,0,1,2,4,0]
    ]


##newArr = []
##for i in range(6):
##    user=[int(i)for i in input().strip().split(' ')]
##    newArr.append(user)
##print(newArr)

# calculating the hourgass sum
def hourglass_sum(arr,row,col):
    sum = 0
    sum += arr[row-1][col-1]
    sum += arr[row-1][col]
    sum += arr[row-1][col+1]
    sum += arr[row][col]
    sum += arr[row+1][col-1]
    sum += arr[row+1][col]
    sum += arr[row+1][col+1]
    return sum

max_hourglass_sum = -63
# index 0 of row and col dnt have hourglass
for row in range(1,len(arr)-1):
    for col in range(1,len(arr)-1):
        current_value = hourglass_sum(arr,row,col)
        if current_value > max_hourglass_sum:
            max_hourglass_sum = current_value
print(max_hourglass_sum)
