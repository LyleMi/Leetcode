class Solution(object):

    M = ("", "M", "MM", "MMM")
    C = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
    X = ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
    I = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")

    def intToRoman(self, num):
        return self.M[num/1000] + self.C[(num / 100) % 10] + self.X[(num / 10) % 10] + self.I[num % 10]
