class Solution(object):

    def isIsomorphic(self, s, t):
        return len(s) == len(t) and len(set(t)) == len(set(s)) == len(set(zip(s, t)))
