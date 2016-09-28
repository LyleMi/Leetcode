class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        return ((C - A) * (D - B) + (G - E) * (H - F)) - reduce(lambda x, y: (x*y*(x > 0 and y > 0)), (min(C, G) - max(A, E), min(D, H) - max(B, F)))
