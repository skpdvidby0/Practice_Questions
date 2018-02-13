# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2 = 0, 0
        a, b = headA, headB
        while a and a.next:
            a = a.next
            p1 += 1
        while b and b.next:
            b = b.next
            p2 += 1
        if a != b:
            return None
        short = headA if p1 <= p2 else headB
        long1 = headA if p1 > p2 else headB
        diff = abs(p1 - p2)
        count = diff
        while count != 0 and long1 and long1.next:
            long1 = long1.next
            count -= 1
        try:
            while long1 != short:
                long1 = long1.next
                short = short.next
            return short
        except:
            return None
########################Simple solution##########################
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        a, b = headA, headB
        while (a != b):
            a = a.next if a else headB
            b = b.next if b else headA
        return a