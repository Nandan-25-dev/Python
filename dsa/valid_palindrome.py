class Solution:
    def __init__(self,s):
        self.s=s
    def valid_palindrome(self):
        self.s=''.join(c.lower() for c in self.s if c.isalnum())
        return self.s==self.s[::1]
test=Solution("A man a plan a canal: panama")
print(test.valid_palindrome())