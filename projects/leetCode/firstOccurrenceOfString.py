# Given two strings needle and haystack,
#  return the index of the first occurrence of needle in haystack
# , or -1 if needle is not part of haystack.

needle = "sad"
haystack = "sadbutsad"

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        
        index = haystack.find(needle)
        return index

answer = Solution()

print(answer.strStr(haystack,needle))

