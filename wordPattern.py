class Solution(object):
    def wordPattern(self, pattern, str):
        s = str.split()
        z = zip(list(pattern),s)
        return len(s) == len(pattern) and len(set(z)) == len(set(s)) == len(set(map(lambda i:i[0],z))) 