class Solution:
    def isPalindrome(self, s: str) -> bool:
        noSpaces = ""
        for c in s:
            if c.isalnum():
                noSpaces += c.lower()

        right = len(noSpaces)-1
        for left in range(len(noSpaces)//2):
            if noSpaces[left] != noSpaces[right]:
                return False
            right-=1
        return True
            