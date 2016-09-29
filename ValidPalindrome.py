class Solution(object):
    def isPalindrome(self, s):
        return (lambda x: x == x[::-1])(filter(lambda i: i.isalnum(), s.lower()))
