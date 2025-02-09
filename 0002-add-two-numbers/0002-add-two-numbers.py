class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()  # Dummy node to start the result list
        current = dummy  # Pointer to build the result list
        carry = 0  # Variable to keep track of carry

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10  # Carry for the next iteration
            current.next = ListNode(total % 10)  # Create new node with digit
            current = current.next  # Move to the next node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # Return the next node after dummy
