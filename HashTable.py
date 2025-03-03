from LinkList import SLL, Node

class HashTable:
    def __init__(self, size):
        self.size = size
        self.arr=[SLL() for i in range(self.size)]

    def __get_hash(self, key):
        index = 0
        for char in key:
            index += ord(char)
        return index % self.size

    def put(self, key, data):
        primary_index = self.__get_hash(key)
        if self.arr[primary_index] is None:
            self.arr[primary_index] = data
            return True
        else:
            secondary_index = self.__get_second_hash(key)
            if self.arr[secondary_index] is None:
                self.arr[secondary_index] = data
                return True
            else:
                print("Hash Table Collision, Data NOT Saved")
                return False

    def putSLL(self, key, data):
        primary_index = self.__get_hash(key)
        self.arr[primary_index].prepend(data)

    def removeSLL(self, key):
        index = self.__get_hash(key)
        self.arr[index].delete(key)
        return True

    def get(self, key):
        index = self.__get_hash(key)
        return self.arr[index]

    def putSelfHash(self, data):
        primary_index = hash(data) % self.size
        self.arr[primary_index].prepend(data)

    def removeSelfHash(self, data):
        primary_index = hash(data) % self.size
        self.arr[primary_index].delete(data)

    def getSelfHash(self,data):
        primary_index = hash(data) % self.size
        found = self.arr[primary_index].get(data)
        return found


    def __str__(self):
        result = ""
        for sll in self.arr:
            if sll is not None:
                result += str(sll) + "\n"
        return result



    # def __get_second_hash(self, key):
    #     index = 0
    #     for char in key:
    #         index += ord(char)
    #     return (index * 17 + 1) % self.size