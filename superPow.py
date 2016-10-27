class Solution(object):

    def superPow(self, a, b):
        n = reduce(lambda x, y: x*10 + y, b)
        a %= 1337
        b = 1
        i = map(int, bin(n)[2:][::-1])
        for k in i:
            b = (b*a**k) % 1337
            a = (a*a) % 1337
        return b


'''
desc 

 Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8

Example2:

a = 2
b = [1,0]

Result: 1024

---

actualy, python implement Modular repeat square remainder algorithm

so

return pow(a, reduce(lambda x,y:x*10 + y,b), 1337)

could be a solution

---

if you know more about number theory

return 0 if a % 1337 == 0 else pow(a, reduce(lambda x, y: (x * 10 + y) % 1140, b) + 1140, 1337)

could be faster

'''