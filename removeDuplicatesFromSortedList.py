class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head):
    while head is not None:
        print(f"{head.val}", end="")
        if head.next is not None:
            print(" -> ", end="")
        head = head.next
    print()

def deleteDuplicates(head):
    dummy = head
    if head is not None:
        while head.next is not None:
            if head.next is not None:
                if head.next.val != head.val:
                    head = head.next 
                else:
                    head.next = head.next.next
    
        return dummy

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)


result = deleteDuplicates(head)

printList(result)