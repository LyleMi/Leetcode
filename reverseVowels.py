class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        vowels = 'aeiouAEIOU'
        left = 0
        right = len(s) - 1
        while right > left:
            while left < right and s[left] not in vowels:
                left +=1
            while right > left and s[right] not in vowels:
                right -= 1
            s[right], s[left] = s[left], s[right]
            left += 1
            right -= 1
        return ''.join(s)