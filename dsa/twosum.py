class Solution(object):
    def __init__(self,nums,target):
        self.nums=nums
        self.target=target
    def twosum(self):
        seen={}
        for i,num in enumerate(self.nums):
            needed=self.target-num
            if needed in seen:
                return [seen[needed],i]
            seen[num]=i
t1=Solution([2,7,11,13],9)
print(t1.twosum())
