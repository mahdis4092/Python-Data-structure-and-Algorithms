'''
class Node:
    def __int__(self,data):
        self.data=data
        self.next_node=None

    def __repr__(self):
        return str(self.data)

class Linkedlist:
    def __int__(self):
        self.head=None
        self.num_of_node=0

    def insert_start(self,data):
        self.num_of_node+=1
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
        else:
            new_node.next_node=self.head
            self.head=new_node

    def insert_end(self,data):
        self.num_of_node+=1
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
        else:
            actual_node=self.head
            while actual_node.next_node is not None:
                actual_node=actual_node.next_node

            actual_node.next_node=new_node

    def size_of_list(self):
        return self.num_of_node

    def traverse(self):
        actual_node=self.head
        while actual_node is not None:
            print(actual_node)
            actual_node=actual_node.next_node

if __name__=='__main__':
    linked_list=Linkedlist()
    linked_list.insert_end(10)
    linked_list.insert_start(100)
    linked_list.insert_start(90)


def rotate_array(arr,n,d):
    temp=[]
    i=0
    while i<d:
        temp.append(arr[i])
        i+=1
    i=0
    while d<n:
        arr[i]=arr[d]
        i+=1
        d+=1
    arr[:]=arr[:i]+temp
    return arr[:]

arr=[1,2,3,4,5,6,7]
print("Array after left rotation : ",end=" ")
print(rotate_array(arr,len(arr),3))


'''
A = []
n=int(input())
for i in range(0, n):
    j = input().split()
    cout = 0

    if j.count('1') >= 2:
        cout += 1
        A.append(cout)
print(sum(A))

#print(final_count)
        #print(final_count)
   # matrix.append(A)


#print(final_count)













       # if A[j]==1:
          #  count+=1



  #  x=int(input())
   # A.append(x)
#print(A)