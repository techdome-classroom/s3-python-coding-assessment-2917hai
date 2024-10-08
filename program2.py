
    class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Map of Roman numerals to their integer values
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Initialize the result
        total = 0
        
        # Loop through the string
        for i in range(len(s)):
            # If the current value is less than the next one, we subtract it
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        
        return total
 pass


