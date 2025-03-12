import random
import string
import sys
import time

from HashTable import HashTable
from BST import BST
from Book import Book
from datetime import datetime
sys.setrecursionlimit(2000)  # Increase the recursion limit to 2000
bst = BST()
isbn_set = set()
known_isbn = 0
books = [];

def generate_random_isbn():
    """ Generates a random 13-digit ISBN """
    return ''.join(random.choices(string.digits, k=13))

def generate_random_title():
    """ Generates a random book title """
    words = ["Python", "Data", "Algorithms", "Structures", "AI", "Deep Learning", "Code", "Design", "Patterns"]
    return " ".join(random.choices(words, k=random.randint(2, 5)))

# ****************************************************************
# Array Testing
# ****************************************************************

startInsert_timeAR = time.time()

for i in range(1, 1000):
    isbn = generate_random_isbn()
    title = generate_random_title()
    book = Book(isbn, title)
    books.append(book)
    if i == 999:
        known_isbn = isbn

endInsert_timeAR = time.time()
print ("Array Insert Time: " + f"{endInsert_timeAR - startInsert_timeAR:.9f}")

searchARBook = Book(known_isbn, "TTTTT")

startSearch_timeAR = time.time()

for book in books:
    if (book == searchARBook):
        print (book)
        break

endSearch_timeAR = time.time()
print ("Array Search Time: " + f"{endSearch_timeAR - startSearch_timeAR:.9f}" + "\n\n")

# ****************************************************************
# BST Testing
# ****************************************************************

startInsert_timeBST = time.time()

for i in range(1000000):
    while True:
        isbn = generate_random_isbn()
        if isbn not in isbn_set:
            isbn_set.add(isbn)
            break

    title = generate_random_title()
    book = Book(isbn, title)

    if i == 999999:
        known_isbn = isbn

    bst.insert(book)

endInsert_timeBST = time.time()
print ("BST Insert Time: " + f"{endInsert_timeBST - startInsert_timeBST:.9f}")

searchBook = Book(known_isbn, "")

# Search for the known ISBN and measure time
startSearch_timeBST = time.time()
found_book = bst.search(searchBook)
endSearch_timeBST = time.time()
print ("BST Search Time : " + f"{endSearch_timeBST - startSearch_timeBST:.9f}")

print(found_book)

# ****************************************************************
# BST Testing (post Rebalance
# ****************************************************************
print ("Height of Tree(Original): " + str(bst.height(bst.root)))
bst.rebalance()
print ("Height of Tree(Rebalanced): " + str(bst.height(bst.root)))

start_timeRB = time.time()
found_book = bst.search(searchBook)
end_timeRB = time.time()

print ("Search Time after Rebalance : " + f"{end_timeRB - start_timeRB:.9f}")




