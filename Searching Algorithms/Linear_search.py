A=[]
s_data=32
is_found=False
n=int(input("Enter the size of an array"))
for i in range(n):
    l=int(input())
    A.append(l)
print(A)
for num in range(n):
    if A[num]==s_data:
        is_found=True
        break
if  is_found: #check is_found update as true 
    print("found")
else:
    print("Not Found")



