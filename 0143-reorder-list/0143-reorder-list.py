# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        current = slow
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        first, second = head, prev
        while second.next:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2

def create_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(elements)