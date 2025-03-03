class Book:



    def __init__(self, isbn=1, title="no title"):
        self.isbn = isbn
        self.title = title

    def __str__(self):
        text = ""
        text += self.title + " : "
        text += str(self.isbn)
        return text

        #Changing the functionality of the gt, for python to sort object
    def __gt__(self, other):
        return self.isbn > other.isbn

    def __lt__(self, other):
        return self.isbn < other.isbn

    def __eq__(self, other):
        return self.isbn == other.isbn

    def __hash__(self):
        return self.isbn % 31