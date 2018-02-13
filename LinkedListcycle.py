class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next

            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

########################faster code same concept##########################
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False