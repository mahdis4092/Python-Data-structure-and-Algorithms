'''

def create_stack():
    stack=[]
    return stack
def IsEmpty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print(item +" Item push on the stack")
def pop(stack):
    if len(stack)==0 :
        return str(-1)
    else:
       return stack.pop()
def peek(stack):
    if len(stack)==0:
        return str(-1)
    else:
        return stack[len(stack)-1]





stack=create_stack()
push(stack,str(10))
push(stack,str(20))
push(stack,str(30))
push(stack,str(40))
print(pop(stack) + "pop from stack")
print(peek(stack) + "peek item from stack")
'''
'''
class Node:

    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.right_node = None
        self.left_node = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # we have to go to the left subtree
        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
        # we have to visit the right subtree
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):

        if node.left_node:
            self.traverse_in_order(node.left_node)

        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)


if __name__ == '__main__':

     bst = BinarySearchTree()
     bst.insert(5)
     bst.insert(3)
     bst.insert(6)
     bst.insert(1)
     bst.traverse()
'''