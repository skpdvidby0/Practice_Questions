"""First, if nums[m] > nums[r] then the sequence change number will be between m and r.
Second, if nums[m] < nums[r], then the sequence change number will be between l and m.
Third, if there exist duplicates and result in nums[m]==nums[r] 
then we will not know that that sequence change number but 
one thing for sure, nums[r] will not be the minimum so we can
just move the r backward to eliminate nums[r] by r--, which can
then be able to terminate the searching properly."""

def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    j = len(nums) - 1
    while i < j:
        m = i + (j - i) / 2
        if nums[m] > nums[j]:
            i = m + 1
        else:
            j = m
    return nums[i]

nums=[2,1]
print findMin(nums)



# while i<j:
#     m=i+(j-i)/2
#     if nums[m]>nums[j]:
#         i=m+1
#     else:
#         j=m
#