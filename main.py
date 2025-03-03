from StackX import StackX
from QueueX import QueueX
from LinkList import Node, SLL
from Book import Book
from HashTable import HashTable
from BST import BST, Node




bst = BST()

# book1 = Book(1111, "Book1")
# book2 = Book(2387, "Book2")
# book3 = Book(3423, "Book3")
# book4 = Book(4443, "Book4")
# book5 = Book(5555, "Book5")

bst.insert(10)
bst.insert(12)
bst.insert(8)
bst.insert(6)
bst.insert(9)

bst.inorder_traversal()




# ht.putSelfHash(book1)
# ht.putSelfHash(book2)
# ht.putSelfHash(book3)
# ht.putSelfHash(book4)
# ht.putSelfHash(book5)
#
# # targetBook = Book(54321, "")
# # ht.removeSelfHash(targetBook)
#
# print(ht)