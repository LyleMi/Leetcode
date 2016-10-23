class Solution(object):

    def originalDigits(self, s):
        c = [s.count(i) for i in ['z', 'o', 'w', 'h', 'u', 'v', 'x', 's', 'g', 'i']]

        c[7] -= c[6]
        c[3] -= c[8]
        c[5] -= c[7]
        c[1] -= (c[0] + c[2] + c[4])
        c[9] -= (c[5] + c[6] + c[8])

        return ''.join(map(lambda i: str(i) * c[i], range(10)))
