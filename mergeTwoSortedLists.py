class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(node):
    while node is not None:
        print(f"{node.val}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()

def mergeLists(head1, head2):
    sortedList = []
    
    while head1 is not None:
        sortedList.append(head1.val)
        head1 = head1.next

    while head2 is not None:
        sortedList.append(head2.val)
        head2 = head2.next

    sortedList.sort()

    dummy = ListNode(-1)
    curr = dummy

    for value in sortedList:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next
    
list1 = ListNode(5)
list1.next = ListNode(10)
list1.next.next = ListNode(15)
list1.next.next.next = ListNode(40)

list2 = ListNode(2)
list2.next = ListNode(3)
list2.next.next = ListNode(20)

result = mergeLists(list1, list2)

printList(result)