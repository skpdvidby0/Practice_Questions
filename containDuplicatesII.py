
def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict={}
        for counter,value in enumerate(nums):
            if value in dict and counter-dict[value]<=k:
                return True
            dict[value]=counter
        return False