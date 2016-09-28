class Solution(object):
    def grayCode(self, n):
        result = [0]
        for i in range(n):
            result.extend([x + 2**i for x in result[::-1]])
        return result