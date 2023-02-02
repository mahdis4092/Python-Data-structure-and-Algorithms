import math
def binarysearch(arr, n, left, right):
    while left <= right:
        mid = math.floor((left+right)/2)
        if n == arr[mid]:
            return mid
        elif n>arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

pre_arr=[2,5,8,7,54,1,6,21,12,31,11]
arr=sorted(pre_arr)
print(arr)
n=21
x=binarysearch(arr,n,0,len(arr)-1)
#print(x)
if x!=-1:
    print(f"Element is present at {x} index position")
else:
    print("Element not found")

