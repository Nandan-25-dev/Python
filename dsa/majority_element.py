class Solution:
    def __init__(self,nums):
        self.nums=nums
    def majority_element(self):
        count={}
        for n in self.nums:
            count[n]=count.get(n,0)+1
            if count[n]>len(self.nums)//2:
                return n
test=Solution([3,2,3])
print(test.majority_element())
