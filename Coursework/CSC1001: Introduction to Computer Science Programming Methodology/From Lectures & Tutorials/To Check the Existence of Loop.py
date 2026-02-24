def has_loop(head):
    slow = head
    fast = head
    while fast.pointer:
        slow = slow.pointer
        fast = fast.pointer.pointer
        if slow == fast:
            return True
    return False