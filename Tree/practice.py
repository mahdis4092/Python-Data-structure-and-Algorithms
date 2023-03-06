class Node:
    def __init__(self,data,parent=None):
        self.data=data
        self.left_node=None
        self.right_node=None
        self.parent=parent

class Binarytree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)




    def insert_node(self,data,node):
        if data<node.data:
            if node.left_node is not None:
                self.insert_node(data,node.left_node)
            else:
                node.left_node=Node(data,Node)
        else:
            if node.right_node is not None:
                self.insert_node(data,node.right_node)
            else:
                node.right_node = Node(data, Node)

    def get_min(self):
        #check node is not null
        if self.root:
            return self.get_min_value(self.root)
    def get_min_value(self,node):
        if node.left_node:
            return self.get_min_value(node.left_node)

        return node.data

    def get_max(self):
        # check node is not null
        if self.root:
            return self.get_max_value(self.root)

    def get_max_value(self, node):
        if node.right_node:
            return self.get_max_value(node.right_node)

        return node.data

    def traverse(self):
        self.traverse_in_order(self.root)

    def traverse_in_order(self,node):
        if node.left_node:
            self.traverse_in_order(node.left_node)
        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)


if __name__ == '__main__':
    bst=Binarytree()
    bst.insert(10)
    bst.insert(-5)
    bst.insert(20)
    bst.insert(12)
    bst.insert(15)

    bst.get_max()

    bst.traverse()
    bst.get_max()







