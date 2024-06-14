"""
You are given an integer array nums. 
In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.
"""

from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        nums.sort()

        moves = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                # calculate the difference between the previous element and the current element
                shifted = nums[i - 1] - nums[i] + 1
                # increment the current element by the difference
                nums[i] += shifted
                # increment the moves by the difference
                moves += shifted

        return moves
