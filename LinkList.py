class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, value):
        # If this is the first element:
        if self.head == None:
            self.head = Node(value)

        # If this is any subsequent element
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def display(self):
        elements = []
        current = self.head

        while current is not None:
            elements.append(current.value)
            current = current.next

        print(elements)

    def prepend(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            new_head = Node(value)
            new_head.next = self.head
            self.head = new_head


    def delete(self, value):
        current = self.head
        prev = None
        #if current is first node and it is the value
        if current is not None and current.value == value :
            self.head = current.next
            return

        while current is not None and current.value != value :
            prev = current
            current = current.next

        if current is None :
            print("Value not found")
            return

        prev.next = current.next

    def insert_sorted(self, data):
        new_node = Node(data)

        if self.head is None or self.head.value > data:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        while current.next is not None and current.next.value < data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def __str__(self):
        # Return a string representation of the linked list
        elements = ""
        current = self.head

        if self.head is None:
            return "Empty List"

        while current is not None:
            elements += str(current.value) + " -> "
            current = current.next
        return elements

    def if_exist(self, data):
        current = self.head

        while current is not None:
            if current.value == data:
                return True
            current = current.next
        return False


    # To search for books in the link list a search_book placeholder will need to be created
    # Then passed into the get() function with an isbn to search for
    def get(self, data):
        current = self.head
        while current is not None:
            if current.value == data:
                return current.value
            current = current.next
        return False

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
