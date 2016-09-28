class Solution(object):
    def plusOne(self, digits):
        digits[-1] += 1    
        for i in xrange(len(digits)-1,-1,-1):
            if digits[i] > 9:
                digits[i] -= 10
                if i > 0:
                    digits[i-1] += 1
                else:
                    digits = [1] + digits
                    break
            else:
                break
        return digits
        
#return map(int,list(str(int(''.join(map(str, digits)))+1)))