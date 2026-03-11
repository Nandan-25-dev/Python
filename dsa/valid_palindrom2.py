class Solution:
    def __init__(self,s):
        self.s=s
    def valid_pal2(self):
        def check(l,r):
            while l<r:
                if self.s[l]!=self.s[r]:
                    return False
                l+=1
                r-=1
            return True
        left=0
        right=len(self.s)-1
        while left<right:
            if self.s[left]<self.s[right]:
                return check(left+1,right) or check(left,right-1)
            left+=1
            right-=1
        return True
test=Solution('abcc')
print(test.valid_pal2())
