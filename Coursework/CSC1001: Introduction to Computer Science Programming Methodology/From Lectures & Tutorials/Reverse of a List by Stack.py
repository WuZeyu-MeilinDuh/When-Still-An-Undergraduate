from Stack import Stack

def reverse(lst):
    s = Stack()
    new = list()
    for i in lst:
        s.push(i)
    while not s.is_empty():
        new.append(s.pop())
    return new
