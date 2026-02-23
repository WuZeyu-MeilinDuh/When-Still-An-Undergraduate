# Question 1: Merge two Sorted Linked List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    '''
    Please DO NOT modify the given function except the TODO part.
    This function is used to merge two ordered linked lists.
    :parameter: l1, l2 are heads of two sorted linked lists.(l1 and l2 are sorted in non-decreasing order.)
    :return: head node of merged linked list
    '''
    # TODO part
    # ------- Your code start here -------

    v1 = l1.val
    v2 = l2.val
    if v1 >= v2:
        node_to_be_returned = node_a = l2
        node_b = l1
    else:
        node_to_be_returned = node_a = l1
        node_b = l2
    node_A = node_a.next
    while node_b and node_A:
        while node_A:
            if node_b.val >= node_A.val:
                node_A = node_A.next
                node_a = node_a.next
            else:
                break
        spare_node = node_b.next
        node_b.next = node_A
        node_a.next = node_b
        node_b = spare_node
        if node_A:
            node_A = node_a.next
    if not node_A and node_b:
        node_a.next.next = node_b

    # ------- End of your code -----------

    # ------- return head node -----------
    return node_to_be_returned


# ------- Helper Functions  -----------
# You can use these helper functions to better complete your homework
def printList(head:ListNode):
    '''
    This function is used to print the node values of the linked list.
    '''
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next


def createList(array: list) -> ListNode:
    '''
    This function is used to create a new linked list from a list.
    '''
    if not array:
        return []
    head = ListNode(array[0])
    current = head
    for value in array[1:]:
        new_node = ListNode(value)
        current.next = new_node
        current = new_node
    return head


if __name__ == '__main__':
    # examples
    list1 = [1,2,4]
    list2 = [1,3,4]
    linked1 = createList(list1)
    linked2 = createList(list2)


    head = mergeTwoLists(linked1, linked2)
    printList(head)