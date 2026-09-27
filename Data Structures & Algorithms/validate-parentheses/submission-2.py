class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        stack = []
        for bracket in s:
            if bracket in closeToOpen:
                if not stack:
                    return False
                top = stack.pop()
                if closeToOpen[bracket]!=top:
                    return False
            else:
                stack.append(bracket)
        
        return False if stack else True