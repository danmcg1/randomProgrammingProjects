# Given a string s consisting of words and spaces,
#  return the length of the last word in the string.

# A word is a maximal consisting of non-space characters only.

s = "   fly me   to   the moon  "

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        length = len(words[-1])
        if len(words[-1]) == 0:
            return 0
        else:
            return length

answer = Solution()

print(answer.lengthOfLastWord(s))