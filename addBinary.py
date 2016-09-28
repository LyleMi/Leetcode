class Solution(object):
    def addBinary(self, a, b):
        return bin(eval('0b'+a+'+'+'0b'+b))[2:]