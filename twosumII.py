class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        l=0
        r=len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                res.append(l+1)
                res.append(r+1)
                return res
            elif numbers[r]+numbers[l]>target:
                r=r-1
            else:
                l=l+1
        return res