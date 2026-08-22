# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

# 1 -> 1
# 2 -> 2
# 3 -> 3
# 4 -> 5
# 5 -> 8

# [2,2,1]
# [1,2,2]
# [2,1,2]
# [1,1,1,1,1]
# [1,1,1,2]
# [1,1,2,1]
# [1,2,1,1]
# [2,1,1,1]

n = 45

numbers = [1,1]

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return(0)
        elif n == 1:
            return(1)
        elif n == 2:
            return(2)
        else:
            for i in range(1,n):
                new_number = numbers[i-1]+numbers[i]
                numbers.append(new_number)
            return(numbers[-1])

answer = Solution()

print(answer.climbStairs(n))