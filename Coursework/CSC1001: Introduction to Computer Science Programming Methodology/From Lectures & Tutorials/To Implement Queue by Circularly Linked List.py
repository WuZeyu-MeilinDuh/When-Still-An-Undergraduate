from Node import Node

# Personal try
class Circularly_Linked_Queue:
    def __init__(self):
        self.__size = 0
        self.__tail = None
        self.__head = None

    def is_empty(self):
        return self.__size == 0

    def first(self):
        if self.is_empty():
            print('The queue is empty.')
        else:
            answ = self.__tail.element
            return answ

    def enqueue(self, elem):
        if self.is_empty():
            self.__head = Node(elem, None)
            self.__tail = self.__head
            self.__head.pointer = self.__tail
            self.__tail.pointer = self.__head
        else:
            self.__head = Node(elem, self.head)
            self.__tail.pointer = self.__head
            self.__size = self.__size + 1

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            resu = self.__tail.element
            if self.__size > 1:
                target = self.__tail
                for i in range(self.__size - 1):
                    target = target.pointer
                target.pointer = self.__head
                self.__tail = target
                self.__size = self.__size - 1
            else:
                self.__head = None
                self.__tail= None
                self.__size = 0
            return resu

# Teacher's version
class C_Queue:
    def __init__(self):
        self.__size = 0
        self.__tail = None

    def __length__(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def first(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            head = self.__tail.pointer
            return head.element

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            old_head = self.__tail.pointer
            if self.__length__() == 1:
                self.__tail = None
            else:
                 self.__tail.pointer = old_head.pointer
            self.__size = self.__size - 1
            return old_head.element

    def enqueue(self,e ):
        new = Node(e, None)
        if self.__size == 1:
            self.__tail = new
        else:
            new.pointer = self.__tail.pointer
            self.__tail.pointer = new
        self.__tail = new
        self.__size = self.__size + 1
        