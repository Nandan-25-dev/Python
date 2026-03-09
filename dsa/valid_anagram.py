class Solution:
    def __init__(self,s,t):
        self.s=s
        self.t=t
    def Valid_anagram(self):
        if (len(self.s)!=len(self.t)):
            return False
        count={}
        for c in self.s:
            count[c]=count.get(c,0)+1
        for c in self.t:
            if c not in count:
                return False
            count[c]-=1
        return True
result=Solution('apple','fruit')
print(result.Valid_anagram())