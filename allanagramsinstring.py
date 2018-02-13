class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = self.getcount(s)
        for i in s:
            if count[ord(i)] == 1:
                return s.index(i)
        return -1

    def getcount(self, s):
        count = [0] * 256
        for i in s:
            count[ord(i)] += 1
        return count