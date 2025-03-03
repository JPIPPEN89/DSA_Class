
class QueueX:

    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.tail = -1
        self.head = 0

    def is_full(self):
       return self.tail == (self.size - 1)

    def is_empty(self):
        return (self.tail == -1)

    def enqueue(self, item):
        if self.is_full():
             print("Queue is full")
        else:
             self.tail += 1
             self.queue[self.tail] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            item = self.queue[self.head]
            new_list = [None] * self.size

            for i in range(1,self.tail+1) :
                new_list[i-1] = self.queue[i]

            self.queue = new_list
            self.tail -=1
            return self.queue

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.queue[self.head])

    def display(self):
        print(self.queue)


    def __str__(self):
        if self.is_empty():
            return ""
        else:
            txt = ""
            for i in range(0, self.tail + 1):
                txt += str(self.queue[i]) + " : "
            return txt
