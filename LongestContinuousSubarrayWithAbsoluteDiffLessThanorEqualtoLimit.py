"""
Given an array of integers nums and an integer limit, 
return the size of the longest non-empty subarray 
such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """ """
        res = 0
        i = 0
        j = 0
        n = len(nums)
        minq = []
        maxq = []

        while j < n:
            # keep the min and max value in the window
            # if the current value is smaller than the last value in minq, pop the last value
            # until the last value in minq is smaller than the current value
            while minq and minq[-1] > nums[j]:
                minq.pop()
            minq.append(nums[j])

            # if the current value is larger than the last value in maxq, pop the last value
            # until the last value in maxq is larger than the current value
            while maxq and maxq[-1] < nums[j]:
                maxq.pop()
            maxq.append(nums[j])

            # if the difference between the max value and min value in the window is larger than limit
            # move i to the right
            while maxq[0] - minq[0] > limit:
                if minq[0] == nums[i]:
                    minq.pop(0)
                if maxq[0] == nums[i]:
                    maxq.pop(0)
                i += 1

            # update the result
            res = max(res, j - i + 1)
            j += 1

        return res


if __name__ == "__main__":

    sol = Solution()

    nums1 = [8, 2, 4, 7]
    limit1 = 4

    res = sol.longestSubarray(nums1, limit1)  # Output: 2
    print(res)

    nums2 = [10, 1, 2, 4, 7, 2]
    limit2 = 5

    res = sol.longestSubarray(nums2, limit2)  # Output: 4
    print(res)

    nums3 = [4, 2, 2, 2, 4, 4, 2, 2]
    limit3 = 0

    res = sol.longestSubarray(nums3, limit3)  # Output: 3
    print(res)
