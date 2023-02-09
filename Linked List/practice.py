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
'''