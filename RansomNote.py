class Solution(object):

    def canConstruct(self, ransomNote, magazine):
        for i in range(128):
            if magazine.count(chr(i)) - ransomNote.count(chr(i)) < 0:
                return False
        return True
