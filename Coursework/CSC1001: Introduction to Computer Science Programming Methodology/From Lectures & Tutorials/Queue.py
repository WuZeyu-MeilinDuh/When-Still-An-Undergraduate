class Queue:
    default_capacity = 5

    def __init__(self):
        self.__data = [None]*Queue.default_capacity
        self.__size = 0
        self.__front = 0
        self.__end = 0

    def __len__(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def first(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            return self.__data[self.__front]

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty.')
            return None
        ans = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front = (self.__front + 1) % Queue.default_capacity
        self.__size = self.__size - 1
        return ans

    def enqueue(self, elem):
        if self.__size == Queue.default_capacity:
            print('Queue is full.')
            return None
        self.__data[self.__end] = elem
        self.__end = (self.__end + 1) % Queue.default_capacity
        self.__size = self.__size + 1

    def outputQ(self):
        print(self.__data)