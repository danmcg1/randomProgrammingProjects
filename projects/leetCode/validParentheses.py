
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.



s = '({[{(())}]})'

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracketBuffer = []
        try:
            for i in s:
                if i == '(':
                    bracketBuffer.append(i)
                elif i == '{':
                    bracketBuffer.append(i)
                elif i == '[':
                    bracketBuffer.append(i)

                elif i == ')' and bracketBuffer[-1] == '(':
                    del bracketBuffer[-1]
                elif i == '}' and bracketBuffer[-1] == '{':
                    del bracketBuffer[-1]
                elif i == ']' and bracketBuffer[-1] == '[':
                    del bracketBuffer[-1]

                elif i == ')' and bracketBuffer[-1] != '(':
                    return(False)
                elif i == '}' and bracketBuffer[-1] != '{':
                    return(False)
                elif i == ']' and bracketBuffer[-1] != '[':
                    return(False)

                elif bracketBuffer == []:
                    return False

        except:
            return(False)
        if bracketBuffer == []:
            return(True)
        else:
            return(False)

solver = Solution()
print(solver.isValid(s))