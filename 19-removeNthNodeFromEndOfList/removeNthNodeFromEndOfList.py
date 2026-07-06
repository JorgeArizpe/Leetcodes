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


def removeNthFromEnd(head: ListNode, n):
    if head.next is None and n > 0:
        return None

    dummy = ListNode(0, head)
    slow = dummy
    fast = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next is not None:
        fast = fast.next
        slow = slow.next
        print("fast", fast.val)
        print("slow", slow.val)

    slow.next = slow.next.next

    return dummy.next


n = 2

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result = removeNthFromEnd(head, n)

printList(result)
