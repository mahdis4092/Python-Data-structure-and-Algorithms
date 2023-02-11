'''
METHOD 2 (Using temp array):
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
A=[1,2,3,4,5,6,7]
Rotation of the above array by 2 will make array
A=[3,4,5,6,7,1,2]
Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
1) Store d elements in a temp array
   temp[] = [1, 2]
2) Shift rest of the arr[]
   arr[] = [3, 4, 5, 6, 7, 6, 7]
3) Store back the d elements
   arr[] = [3, 4, 5, 6, 7, 1, 2]
'''

def rotate_array(arr,n,d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr

arr=[1,2,3,4,5,6,7]
print("Array after left rotation : ",end=" ")
print(rotate_array(arr,len(arr),3))