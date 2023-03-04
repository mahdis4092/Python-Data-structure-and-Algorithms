# code
# Definition for a binary tree node

class Node:

    def __init__(self, data):
        self.data = data

        self.left = None

        self.right = None


class BinaryTree:

    def __init__(self):

        self.root = None

    def add_node(self, data):

        new_node = Node(data)

        # If root is None, assign the new node to the root

        if self.root is None:

            self.root = new_node

        else:

            focus_node = self.root

            parent = None

            while True:

                parent = focus_node

                # If data is less than focus_node, assign focus_node to the left child

                if data < focus_node.data:

                    focus_node = focus_node.left

                    # If there's no left child, assign the new node to the left child

                    if focus_node is None:
                        parent.left = new_node

                        return

                else:

                    focus_node = focus_node.right

                    # If there's no right child, assign the new node to the right child

                    if focus_node is None:
                        parent.right = new_node

                        return

    def pre_order_traversal(self, focus_node):

        if focus_node is not None:
            print(focus_node.data, end=" ")

            self.pre_order_traversal(focus_node.left)

            self.pre_order_traversal(focus_node.right)


# Example usage

tree = BinaryTree()

tree.add_node(50)

tree.add_node(25)

tree.add_node(75)

tree.add_node(12)

tree.add_node(37)

tree.add_node(43)

tree.add_node(30)

tree.pre_order_traversal(tree.root)
'''
explanation
This code defines a binary tree data structure and implements two methods: add_node and pre_order_traversal. The add_node method adds a new node with the given data to the binary tree, while the pre_order_traversal method prints out the data of all the nodes in the tree in pre-order traversal order.

The binary tree is defined using two classes: Node and BinaryTree. The Node class represents a single node in the tree and has three attributes: data, left, and right. The data attribute stores the value of the node, while the left and right attributes point to the left and right child nodes of the current node, respectively. If a node has no left or right child, the corresponding attribute is set to None.

The BinaryTree class is the main class that represents the binary tree data structure. It has a single attribute root, which points to the root node of the tree. The add_node method takes a value as input and adds a new node with that value to the binary tree. If the root node is None, the new node is assigned as the root node. Otherwise, the method searches for the correct position to add the new node by traversing the tree from the root node. If the value of the new node is less than the value of the current node, the method moves to the left child of the current node. If the value of the new node is greater than or equal to the value of the current node, the method moves to the right child of the current node. If the left or right child of the current node is None, the new node is added as the left or right child, respectively.

The pre_order_traversal method takes a node as input and prints out the data of all the nodes in the subtree rooted at that node in pre-order traversal order. Pre-order traversal visits the current node first, then the left subtree, and finally the right subtree. The method recursively calls itself on the left and right child nodes of the current node, if they exist.

Finally, the example usage section creates a new binary tree object, adds several nodes to the tree using the add_node method, and then calls the pre_order_traversal method to print out the data of all the nodes in the tree in pre-order traversal order
'''