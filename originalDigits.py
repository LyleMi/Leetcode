class Solution(object):

    def originalDigits(self, s):
        c = [s.count(i) for i in ['z', 'o', 'w', 'h', 'u', 'v', 'x', 's', 'g', 'i']]

        c[7] -= c[6]
        c[3] -= c[8]
        c[5] -= c[7]
        c[1] -= (c[0] + c[2] + c[4])
        c[9] -= (c[5] + c[6] + c[8])

        return ''.join(map(lambda i: str(i) * c[i], range(10)))

'''
https://leetcode.com/problems/reconstruct-original-digits-from-english/

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:

    Input contains only lowercase English letters.
    Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
    Input length is less than 50,000.

Example 1:

Input: "owoztneoer"

Output: "012"

Example 2:

Input: "fviefuro"

Output: "45"

'''

'''

0, 1, 2,...

some of them has unique str
such as 'z' in 'zero'
and could calc it

'''