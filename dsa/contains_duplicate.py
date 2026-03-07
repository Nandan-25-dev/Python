class Solution(object):
    def __init__(self,nums):
        self.nums=nums
    def containsduplicate(self):
        seen =set()
        for num in self.nums:
            if num in seen:
                return True
            seen.add(num)
        return False
num=Solution([1,2,3,1])
print(num.containsduplicate())