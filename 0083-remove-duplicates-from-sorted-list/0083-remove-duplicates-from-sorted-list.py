# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        
        # Traverse the list until the second last node
        while current and current.next:
            # If the current node's value is equal to the next node's value
            if current.val == current.next.val:
                # Skip the next node by pointing current node's next to the next of next node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the head of the modified list
        return head