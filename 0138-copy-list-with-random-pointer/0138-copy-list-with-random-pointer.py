class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        # Step 1: Insert new nodes in between original nodes
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next, None)
            curr.next = new_node
            curr = new_node.next

        # Step 2: Assign random pointers to the copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the copied list from the original list
        curr = head
        copy_head = head.next
        copy_curr = copy_head
        while curr:
            curr.next = copy_curr.next
            curr = curr.next
            if curr:
                copy_curr.next = curr.next
                copy_curr = copy_curr.next

        return copy_head