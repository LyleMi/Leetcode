class Solution(object):
    def integerBreak(self, n):
        return ((n % 3 + 3 + (n%3 == 2))*3**(n/3-1)) if (n>3) else (n-1)
