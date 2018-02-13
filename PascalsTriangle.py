class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        if numRows==0:
            return []
        for i in range(0,numRows):
            row=[1]
            for _ in range(i):
                row=[x+y for x,y in zip([0]+row,row+[0])]
            res.append(row)
        return res