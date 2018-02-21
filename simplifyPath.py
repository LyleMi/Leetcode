class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stk = []
        for s in path.split("/"):
            if s == "." or s == "":
                continue
            elif s != "..":
                stk.append(s)
            elif len(stk):
                stk.pop()

        return "/" + "/".join(stk)