def largestRectangleArea(height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in xrange(len(height)):
        f=stack[-1]
        print f
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            j= stack[-1]
            print i
            w = i - stack[-1]-1
            print w
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans
largestRectangleArea(height=[2,1,2,3,1])

def lasrgestRectangleArea(height):
    stack=[-1]
    height.append(0)
    ans=0
    for i in xrange(len(height)):
        while height(i)<height(stack[-1]):
            h=height[stack[-1]]
            w=i-stack[-1]-1
            ans=max(ans,h*w)
        stack.append(i)
    heigh.pop()
    return ans
