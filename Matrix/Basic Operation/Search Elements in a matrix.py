'''

Input : mat[][] = [ [1, 5, 9],
                   [14, 20, 21],
                   [30, 34, 43] ]
       x = 14
Output : YES
'''
def search_in_matrix(m,item):
    for i in range(0,3):
        for j in range(0,3):
            if m[i][j]==item:
                return 1
    return


mat=[[1, 5, 9],
         [43, 20, 21],
         [30, 34, 43] ]
x=43
output=search_in_matrix(mat,x)
#check output has any return value
if output :
    print("Yes")
else:
    print("No")