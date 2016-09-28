class Solution(object):

    def countBits(self, num):
        l = [0]
        i = 0
        while True:
            t = len(l)
            for j in xrange(t):
                if i >= num:
                    return l
                l.append(l[j]+1)
                i += 1
