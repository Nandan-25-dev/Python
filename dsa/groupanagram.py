class Solution:
    def __init__ (self,strs):
        self.strs=strs
    def groupanagram(self):
        groups={}
        for word in self.strs:
            key="".join(sorted(word))
            if key not in groups:
                groups[key]=[]
            groups[key].append(word)
        return list(groups.values())
test=Solution(["eat",'ate,','tan','tea'])
print(test.groupanagram())       