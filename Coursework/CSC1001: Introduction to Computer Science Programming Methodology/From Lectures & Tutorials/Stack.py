class Stack:
    def __init__(self):
        self.__data = list()

    def __len__(self):
        return len(self.__data)

    def is_empty(self):
        return self.__len__() == 0

    def push(self, e):
        self.__data.append(e)

    def top(self):
        if self.is_empty():
            print('Stack is empty.')
        else:
            return self.__data[self.__len__() - 1]

    def pop(self):
        if self.is_empty():
            print('Stack is empty.')
        else:
            return self.__data.pop()