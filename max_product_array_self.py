
def product(nums):

    n = len(nums)

    fromBegin = 1;

    fromLast = 1;
    res=[1]*n


    for i in range(n):
        res[i] *= fromBegin;
        fromBegin *= nums[i];
        res[n-1-i] *= fromLast;
        fromLast *= nums[n-1-i];

    return res;
print product(nums=[1,2,3])