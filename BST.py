class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, data):
        current = self.root

        while current is not None:

            if data == current.data:
                return current.data

            elif data < current.data and current.left is None:
                current = current.left

            elif current.right is None and data > current.data:
                current = current.right

            else:
                print("Data Not Found")
                return

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
            if node is None:
                return

        if node.left is not None:
            self.inorder_traversal(node.left)
        print(f"{node.data}")

        if node.right is not None:
            self.inorder_traversal(node.right)