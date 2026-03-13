class Solution:
    def __init__(self,num,target):
        self.num=num
        self.target=target
    def twosum_2(self):
        left=0
        right=len(self.num)-1
        while left<right:
            s=self.num[left]+self.num[right]
            if s==self.target:
                return [left+1,right+1]
            elif s<self.target:
                left+=1
            elif s>self.target:
                right-=1
test=Solution([2,7,9,11,13],20)
print(test.twosum_2())