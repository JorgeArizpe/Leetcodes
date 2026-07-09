class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(head):
    if head is None or head.next is None:
        return None

    slow = head
    fast = head

    while fast:
        for _ in range(2):
            fast = fast.next
            if fast is None:
                return None
        slow = slow.next

        if fast == slow:
            break

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

result = detectCycle(head)

print(result)
