# method A with while loop
def reverseA(head):
    prev = None
    current = head
    while current:
        nex = current.pointer
        current.pointer = prev
        prev = current
        current = nex
    return prev

# method B with recursion
def reverseB(node):
    if not node.pointer:
        return node
    new = reverseB(node.pointer)
    node.pointer.pointer = node
    node.pointer = None
    return new
