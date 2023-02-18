'''
Given a 2D square matrix, print the Principal and Secondary diagonals.
Input:
1 2 3 4
4 3 2 1
7 8 9 6
6 5 4 3
Output:
Principal Diagonal: 1, 3, 9, 3
Secondary Diagonal: 4, 2, 8, 6

The primary diagonal is formed by the elements A00, A11, A22, A33.
Condition for Principal Diagonal: The row-column condition is row = column.

The secondary diagonal is formed by the elements A03, A12, A21, A30.
Condition for Secondary Diagonal: The row-column condition is row = numberOfRows – column -1.
Time Complexity: O(n2), As there is a nested loop involved so the time complexity is squared.
Auxiliary Space: O(1).
'''
def primary_diagonal(M,n):
    print("Primary Diagonal : ", end="")
    for i in range(n):
        for j in range(n):
            if i==j:
                print(M[i][j],end=" ")
    print("")

def secondary_diagonal(M,n):
    print("Secondary Diagonal : ",end="")
    for i in range(n):
        for j in range(n):
            if (i+j)==n-1:
                print(M[i][j],end=" ")

n=4
M=[[1,2,3,4],[4,3,2,1],[7,8,9,6],[6, 5 ,4 ,3]]
primary_diagonal(M,n)
secondary_diagonal(M,n)
