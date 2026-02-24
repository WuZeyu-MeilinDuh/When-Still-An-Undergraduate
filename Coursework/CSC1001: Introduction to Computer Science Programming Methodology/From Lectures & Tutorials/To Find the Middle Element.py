# method A
def find_middle_A(head):
    length = 0
    current = head
    while current:
        current = current.pointer
        length = length + 1
    mid = length // 2
    ind = 0
    to_be_found = head
    while ind < mid:
        to_be_found = to_be_found.pointer
        ind = ind + 1
    return to_be_found

# method B
def find_middle_B(head):
    slow = head
    fast = head
    while fast and fast.pointer:
        slow = slow.pointer
        fast = fast.pointer.pointer
    return slow
