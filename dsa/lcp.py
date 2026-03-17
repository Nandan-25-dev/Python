class Solution:
    def __init__ (self,strs):
        self.strs=strs
    def lcp(self):
        if not self.strs:
            return ""
        for i in range(len(self.strs[0])):
            char=self.strs[0][i]
            for word in self.strs:
                if i>=len(word) or word[i]!=char:
                    return self.strs[0][:i]
        return self.strs[0]
test=Solution(['flower','flow','flight'])
print(test.lcp())