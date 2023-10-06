# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x: int) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        
        current = head
        first = []
        second = []

        while current:
            if current.val < x:
                first.append(current.val)
            else:
                second.append(current.val)
            current = current.next

        keep = ListNode()
        node = keep
        if len(first):
            for i in range(len(first)):
                node.next = ListNode(first[i])
                node = node.next
        
        if len(second):
            for i in range(len(second)):
                node.next = ListNode(second[i])
                node = node.next
        
        def print_list(head):
            current = head
            while current:
                print(current.val)
                current = current.next
        
        print_list(keep.next)
        
        return keep.next

print(Solution().partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3))