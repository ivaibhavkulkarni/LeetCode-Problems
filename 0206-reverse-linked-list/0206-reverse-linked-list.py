# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head

        while current is not None:
            next_temp = current.next  
            current.next = prev       
            prev = current            
            current = next_temp

        return prev  

    def reverseListRecursive(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        reversed_head = self.reverseListRecursive(head.next)
        
        head.next.next = head
        head.next = None  
        return reversed_head 

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