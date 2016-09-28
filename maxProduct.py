class Solution(object):

    def maxProduct(self, words):

        maskLen = {reduce(lambda x, y: x | y, [1 << (ord(c) - 97) for c in word], 0): len(word) 
            for word in sorted(words, key=lambda x: len(x))}.items()
        return max([x[1] * y[1] for i, x in enumerate(maskLen) for y in maskLen[:i] if not (x[0] & y[0])] or [0])
