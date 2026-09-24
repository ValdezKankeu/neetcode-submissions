class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {"]":"[", "}":"{", ")":"("}
        stack = []
        for char in s:
            if char in openToClose:
                if stack and openToClose[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(char)
        
        return len(stack) == 0
        