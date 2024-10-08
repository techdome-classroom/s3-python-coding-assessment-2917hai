class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        # Dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the input string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element is the matching opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all opening brackets were properly closed
        return not stack








    



  

