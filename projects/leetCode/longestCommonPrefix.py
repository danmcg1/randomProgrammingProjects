# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

strs = ["flower","flow","float"]

def singleEnum(list):
    enum = []
    enum += enumerate(list)
    return enum

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]

        for word in strs[1:]:

            while not word.startswith(prefix):
                prefix = prefix[:-1]

            if prefix == "":
                return ""

        return prefix



answer = Solution()
#print(answer.longestCommonPrefix(strs))



def mostEfficientSolution(strs):

    if not strs:
        return ""

    prefix = strs[0]

    for word in strs[1:]:

        while not word.startswith(prefix):
            prefix = prefix[:-1]

        if prefix == "":
            return ""

    return prefix

