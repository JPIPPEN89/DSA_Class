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

        def postorder_traversal(self, node=None):
            if node is None:
                node = self.root
                if node is None:
                    return

            if node.right is not None:
                self.postorder_traversal(node.right)
            print(f"{node.data}")

            if node.left is not None:
                self.postorder_traversal(node.left)

    def remove(self, data):
        current = self.root
        parent = None

        while current is not None and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right

        if current is None:
            return False

        #Case 1 No Child
        if current.left is None and current.right is None:
            if current != self.root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None

        #Case 2 One Child
        elif current.left is None or current.right is None:
            if current.left is not None:
                child = current.left
            else:
                child = current.right

            if current != self.root:
                if parent.left == current:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child

        #Case 3 Two Children
        else:
            successor_parent = current
            successor = current.right

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            current.data = successor.data

            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)


    def inorder_traversalRB(self, node, elements):
        if node is not None:
            self.inorder_traversalRB(node.left, elements)
            elements.append(node.data)
            self.inorder_traversalRB(node.right, elements)

    def sorted_array_to_bst(self, elements):
        if not elements:
            return None
        mid = len(elements)//2
        node = Node(elements[mid])
        node.left = self.sorted_array_to_bst(elements[:mid])
        node.right = self.sorted_array_to_bst(elements[mid+1:])
        return node

    def rebalance(self):
        elements = []
        self.inorder_traversalRB(self.root, elements)
        self.root = self.sorted_array_to_bst(elements)
