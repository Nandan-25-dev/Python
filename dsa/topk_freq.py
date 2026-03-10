class Solution:
    def __init__(self,nums,k):
        self.nums=nums
        self.k=k
    def topk_freq(self):
        freq={}
        for n in self.nums:
            freq[n]=freq.get(n,0)+1
        sorted_items=sorted(freq.items(), key=lambda x: x[1],reverse=True)
        result=[]
        for i in range(self.k):
            result.append(sorted_items[i][0])
        return result
test=Solution([1,1,1,4,4,4,2,3,3,3],3)
print(test.topk_freq())