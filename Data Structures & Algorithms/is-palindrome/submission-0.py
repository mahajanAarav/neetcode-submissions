class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_spaces = ""

        for char in s:
            if char.isalnum():
                no_spaces += char.lower()

        rightP = len(no_spaces) - 1

        for leftP in range(len(no_spaces) // 2):
            if no_spaces[leftP] != no_spaces[rightP]:
                return False
            rightP -= 1

        return True

        
