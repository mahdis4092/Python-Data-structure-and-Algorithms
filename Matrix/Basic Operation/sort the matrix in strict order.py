'''
Given a n x n matrix. The problem is to sort the given matrix in strict order.
Here strict order means that the matrix is sorted in a way such that all elements
in a row are sorted in increasing order and for row ‘i’, where 1 <= i <= n-1, the first element
of row ‘i’ is greater than or equal to the last element of row ‘i-1’.

Input : mat[][] = { {5, 4, 7},
                         {1, 3, 8},
                        {2, 9, 6} }
Output : 1 2 3
         4 5 6
         7 8 9
'''
def sort_matrix(matrix,n):
    temp=[0]*n*n
    k=0
    for i in range(n):
        for j in range(n):
            temp[k]=matrix[i][j]
            k+=1

    temp.sort()
   # print(temp)
    k=0
    for i in range(n):
        for j in range(n):
            matrix[i][j]= temp[k]
            k += 1


def printmatrix(matrix,n):
    for m in range(n):
        for p in range(n):
            print(matrix[m][p],end=" ")
        print("")



matrix=[[5,4,7],[1,3,8],[2,9,6]]
n=3
sort_matrix(matrix,n)
printmatrix(matrix,n)

# Code with explanation here
# Python Implementation to sort the given matrix
def sortMat(mat, n):
    # temporary matrix of size n^2
    temp = [0] * n * n
    k = 0

    # copy the elements of matrix one by one
    # leto temp[]
    for i in range(0, n):
        for j in range(0, n):
            temp[k] = mat[i][j]
            k += 1

    # sort temp[]
    temp.sort(reverse=True)

    # copy the elements of temp[] one by one
    # in mat[][]
    k = 0
    for i in range(0, n):
        for j in range(0, n):
            mat[i][j] = temp[k]
            k += 1


# function to print the given matrix
def printMat(mat, n):
    for i in range(0, n):
        for j in range(0, n):
            print(mat[i][j], end=' ')
        print("")


# Driver program to test above
mat = [[5, 4, 7],
       [1, 3, 8],
       [2, 9, 6]]
n = 3

print("Original Matrix:")
printMat(mat, n)
sortMat(mat, n)
print("\nMatrix After Sorting:")
printMat(mat, n)

# This code is contributed by ishankhandelwals.
