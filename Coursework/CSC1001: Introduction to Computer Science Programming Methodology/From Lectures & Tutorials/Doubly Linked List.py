class Node:
    def __init__(self,element, predecessor, successor):
        self.element = element
        self.predecessor = predecessor
        self.successor = successor

class DLList:
    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.successor = self.trailer
        self.trailer.predecessor = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_between(self, elem, precursor, follower):
        new = Node(elem, precursor, follower)
        new.predecessor.successor = new
        new.successor.predecessor = new
        self.size = self.size + 1
        return new

    def delete(self, node):
        pre = node.predecessor
        beh = node.successor
        pre.successor = beh
        beh.predecessor = pre
        item = node.element
        node.successor = None
        node.predecessor = None
        node.element = None
        self.size = self.size - 1
        return item

    def iterate(self):
        pointer = self.header.successor
        while pointer != self.trailer:
            print(pointer.element)
            pointer = pointer.successor
            