# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next      
            fast = fast.next.next    
            
            if slow == fast:         
                return True
        
        return False  

def create_linked_list(elements, pos=-1):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    cycle_node = None
    
    for i in range(1, len(elements)):
        current.next = ListNode(elements[i])
        current = current.next
        if i == pos:
            cycle_node = current  
        
    if cycle_node:
        current.next = cycle_node  
    
    return head