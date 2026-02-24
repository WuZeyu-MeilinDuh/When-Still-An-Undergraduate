from Node import Node

class Linked_Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, elem):
        self.head = Node(elem, self.head)
        self.size = self.size + 1

    def top(self):
        if self.is_empty():
            print('Stack is empty.')
        else:
            return self.head.element

    def pop(self):
        if self.is_empty():
            print('Stack is empty.')
        else:
            answ = self.head.element
            self.head = self.head.pointer
            self.size = self.size - 1
            return answ