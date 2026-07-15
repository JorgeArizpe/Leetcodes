class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    if not head or not head.next:
        return True

    list  = []

    while head:
        list.append(head.val)
        head = head.next

    n = len(list) - 1

    for i in range(len(list)):
        if list[i] != list[n - i]:
            return False

    return True


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

print(isPalindrome(head))
