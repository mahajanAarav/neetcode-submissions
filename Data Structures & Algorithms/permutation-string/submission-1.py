class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False

        countS1 = {}
        for c in s1:
            countS1[c] = 1 + countS1.get(c, 0)
        
        left = 0 
        countS2 = {}
        for r in range(len(s2)):
            countS2[s2[r]] = 1 + countS2.get(s2[r], 0)

            if r - left + 1 > len(s1):
                countS2[s2[left]] -= 1

                if countS2[s2[left]] == 0:
                    del countS2[s2[left]]

                left += 1

            if countS1 == countS2:
                return True

        return False
            
            
            