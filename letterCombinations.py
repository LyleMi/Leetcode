class Solution(object):
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits):
        res = ['']
        for i in xrange(len(digits)-1, -1, -1):
            res = [s + c for s in self.mapping[digits[i]] for c in res]
        return [res, []][res[0] == '']

if __name__ == '__main__':
    s = Solution()
    print s.letterCombinations("")
    print s.letterCombinations("23")
    print s.letterCombinations("234")
