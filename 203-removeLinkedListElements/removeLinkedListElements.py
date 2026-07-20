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

def removeElements(head, val):
    if not head:
        return head

    newList = []

    while head:
        if head.val != val:
            newList.append(head.val)
        head = head.next

    dummy = ListNode(0)
    head = dummy

    for val in newList:
        head.next = ListNode(val)
        head = head.next

    return dummy.next

val = 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

printList(removeElements(head, val))