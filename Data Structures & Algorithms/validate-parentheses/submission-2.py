class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {
            '(': 0,
            ')': 1,
            '{': 2,
            '}': 3,
            '[': 4,
            ']': 5,
        }
        
        for parentheses in s:
            if dictionary[parentheses] % 2 == 0:
                stack.append(parentheses)
            elif dictionary[parentheses] % 2 == 1 and len(stack) == 0:
                return False
            else:
                open_p = stack.pop()

                if dictionary[parentheses] != dictionary[open_p] + 1:
                    return False

        return len(stack) == 0
