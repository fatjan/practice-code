# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def split_list_to_parts(head: [ListNode], k: int) -> list[[ListNode]]:
    if not head:
        res = []
        for _ in range(k):
            res.append(None)
        return res

    def find_length(head):
        current = head
        res = 0
        while current:
            res += 1
            current = current.next
        
        return res

    len_list = find_length(head)
    
    # find how many nodes per part
    divide = len_list // k
    parts = [divide] * k
    res_divide = len_list % k
    for i in range(res_divide):
        parts[i] += 1
    
    def create_part(head, amount):
        new_node = ListNode()
        current = new_node
        while head and amount:
            node = ListNode(head.val)
            new_node.next = node
            new_node = new_node.next
            head = head.next
            amount -= 1
        
        return [current.next, head]

    res = []
    for i in range(len(parts)):
        if head:
            keep = create_part(head, parts[i])
            element = keep[0]
            head = keep[1]
            res.append(element)
        else:
            res.append(None)                
    return res

head = ListNode()
current = head
for i in range(1, 11):
    node = ListNode(i)
    current.next = node
    current = current.next

split_list_to_parts(head.next, 3)