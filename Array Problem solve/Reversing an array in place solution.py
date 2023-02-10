#Given an array of A-reverse this array in linear running time using constant memory
def reverse(num):
    # pointing the first item
    start_index=0
    # pointing the last item
    end_index=len(num)-1
    while start_index<end_index:
        num[start_index],num[end_index]=num[end_index],num[start_index]
        start_index+=1
        end_index-=1


if __name__ =='__main__':
    n=[1,2,3,4,5]
    reverse(n)
    print(n)



