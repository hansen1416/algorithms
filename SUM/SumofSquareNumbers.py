"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left_pointer = 0
        right_pointer = int(c**0.5)

        while left_pointer <= right_pointer:

            s = left_pointer**2 + right_pointer**2

            if s == c:
                return True

            if s < c:
                left_pointer += 1
            else:
                right_pointer -= 1

        return False


if __name__ == "__main__":

    c = 6

    sol = Solution()
    res = sol.judgeSquareSum(c)

    print(res)

# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
