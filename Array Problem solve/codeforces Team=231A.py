matrix=[]
final_count=0
n=int(input())
for i in range(n):
    count = 0
    A = []
    for j in range(3):
        A.append(int(input()))
        if A[j]==1:
            count += 1
    if count>=2:
        final_count+=1
print(final_count)