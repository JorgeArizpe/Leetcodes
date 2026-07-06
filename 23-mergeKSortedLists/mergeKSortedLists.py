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


def mergeKLists(lists):
    mergedLists = []

    for i in range(len(lists)):
        curr = lists[i]
        while curr is not None:
            mergedLists.append(curr.val)
            curr = curr.next

    mergedLists.sort()

    dummy = ListNode(-1)
    head = dummy

    for value in mergedLists:
        head.next = ListNode(value)
        head = head.next

    return dummy.next


head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(5)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

head3 = ListNode(2)
head3.next = ListNode(6)

lists = [head1, head2, head3]

result = mergeKLists(lists)

printList(result)
