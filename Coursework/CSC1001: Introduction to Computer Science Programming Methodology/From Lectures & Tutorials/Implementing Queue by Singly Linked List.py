from Node import Node

class Linked_Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            return self.head.element

    def enqueue(self, elem):
        new = Node(elem, None)
        if self.is_empty():
            self.head = new
        else:
            self.tail.pointer = new
        self.tail = new
        self.size = self.size + 1

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            answ = self.head.element
            self.head = self.head.pointer
            self.size = self.size - 1
            if self.is_empty():
                self.tail = None
            return answ