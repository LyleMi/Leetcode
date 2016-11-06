class Solution(object):

    def hIndex(self, citations):

        citations = sorted(citations)
        h = 0
        l = len(citations)
        for i in range(l - 1, -1, -1):
            if citations[i] >= l - i:
                h += 1

        return h
