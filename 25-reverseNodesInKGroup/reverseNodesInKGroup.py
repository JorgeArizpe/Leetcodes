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


def reverseKGroup(head, k):
    result = []

    while head is not None:
        curr = []

        while len(curr) < k and head is not None:
            curr.append(head.val)
            head = head.next

        if len(curr) == k:
            curr.reverse()

        result.append(curr)

    result = [number for sublist in result for number in sublist]

    dummy = ListNode(-1)
    head = dummy

    for number in result:
        head.next = ListNode(number)
        head = head.next

    return dummy.next


k = 3

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result = reverseKGroup(head, k)

printList(result)
