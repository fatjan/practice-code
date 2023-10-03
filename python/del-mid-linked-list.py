# using fast slow pointer 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head):
    if head.next == None:
        return head.next
    
    slow, fast = head, head
    before = None
    while fast and fast.next:
        before = slow
        slow = slow.next
        fast = fast.next.next
    
    tmp = before.next.next
    before.next = None
    before.next = tmp
    print('head', head)
    return head

deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))