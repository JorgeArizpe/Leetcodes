class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if head is None or head.next is None:
        return False

    slow = head
    fast = head

    while fast:
        for _ in range(2):
            if fast is None:
                break
            fast = fast.next
        slow = slow.next

        if fast == slow:
            return True

    return False

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

print(hasCycle(head))
