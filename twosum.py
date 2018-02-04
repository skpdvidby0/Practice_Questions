def answer(nums,target):
        pair = []
        num2=[]
        i=0
        while i<=len(nums):
            x = target-nums[i]
            if nums[i] in num2:
                pair.append(nums.index(x))
                pair.append(i)
                print pair
                return pair
            num2.append(x)
            i=i+1
answer(nums,target)