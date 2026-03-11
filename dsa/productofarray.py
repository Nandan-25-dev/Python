class Solution:
    def __init__(self,nums):
        self.nums=nums
    def productofarray(self):
        n=len(self.nums)
        result=[1]*n
        prefix =1
        for i in range(n):
            result[i]=prefix
            prefix*=self.nums[i]
        suffix=1
        for i in range(n-1,-1,-1):
            result[i]*=suffix
            suffix*=self.nums[i]
        return result
test=Solution([1,2,3,4])
print(test.productofarray())
