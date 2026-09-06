# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, 
# it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
import re

s = "A man, a plan, a canal: Panama"

class Solution(object):
    def isPalindrome(self, s: str):
        """
        :type s: str
        :rtype: bool
        """
        if s.isalnum() == True:
            phrase = s.lower().replace(" ", "")
        elif s.isalnum() == False:
            phrase = re.sub(r'[^a-zA-Z0-9]', '', s).lower().replace(" ", "")


        for n in range(int(len(phrase)/2)):
            if str(phrase)[n] != str(phrase)[-(n+1)]:
                return(False)
            else:
                n += 1
        return(True)

answer = Solution()

print(answer.isPalindrome(s))