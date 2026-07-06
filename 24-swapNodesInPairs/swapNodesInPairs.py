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


def swapPairs(head):
    if not head:
        return None

    dummy = head

    if head.next:
        temp = head.val
        head.val = head.next.val
        head.next.val = temp

        if head.next.next:
            head = head.next.next
            head = swapPairs(head)

    return dummy


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

result = swapPairs(head)

printList(result)
