from collections import deque

class StackUsingDoubleQueue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, elem):
        self.q1.append(elem)
        print('The element has been pushed in.')

    def pop(self):
        if self.is_empty():
            print('The simulated stack is empty.')
            return None
        while self.q1.__len__() > 1:
            item = self.q1.popleft()
            self.q2.append(item)
        ans = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return ans

    def top(self):
        if self.is_empty:
            print('The simulated stack is empty.')
            return None
        while self.q1.__len__() > 1:
            self.q2.append(self.q1.popleft())
        tp = self.q1.popleft()
        self.q2.append(tp)
        self.q1, self.q2 = self.q2, self.q1
        return tp

    def is_empty(self):
        return not self.q1