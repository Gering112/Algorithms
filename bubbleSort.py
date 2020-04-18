import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


def bubbleSort(a):
    numOfSwaps = 0 
    length = len(a)-1
    sort = False

    while not sort:
        sort = True
        for i in range(length):
            if a[i] > a[i+1]:
                sort = False
                a[i],a[i+1] = a[i+1],a[i]
                numOfSwaps+=1
    print("Array is sorted in {} swaps.".format(numOfSwaps))
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))

bubbleSort(a)
