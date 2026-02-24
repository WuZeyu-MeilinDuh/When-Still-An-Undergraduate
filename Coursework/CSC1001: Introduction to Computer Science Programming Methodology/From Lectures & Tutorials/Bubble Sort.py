# Bubble-sort a standard list (personal try).
def bubble_my(lst):
    i = len(lst)
    while i > 1:
        i = len(lst)
        for t in range(len(lst) - 1):
            if lst[t] <= lst[t + 1]:
                i = i - 1
            else:
                value = lst[t]
                lst[t] = lst[t + 1]
                lst[t + 1] = value
    return lst

# Bubble-sort a standard list (teacher's version).
def bubble_official(lst):
    length = len(lst)
    while length > 0:
        for i in range(length - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        length = length - 1
    return lst

# Bubble-sort a singly linked list.
def bubble_sll(queue):
    for i in range(queue.length):
        node = queue.head
        while node.pointer:
            if node.element > node.pointer.element:
                node.element, node.pointer.element = node.pointer.element, node.element
            node = node.pointer
    return queue

lst = [4, 2, 45, 87, 9, 21]
print(bubble_official(lst))