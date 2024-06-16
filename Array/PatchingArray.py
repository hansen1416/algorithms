"""
Given a sorted integer array nums and an integer n, add/patch elements to the array 
such that any number in the range [1, n] inclusive can be formed 
by the sum of some elements in the array.

Return the minimum number of patches required.
"""

from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # Initialize a variable miss to 1
        # representing the smallest number that cannot be formed using the current elements in nums.
        miss = 1
        # Initialize the number of patches added
        # keep track of the number of patches added
        patches = 0

        i = 0
        # Loop until `miss` is greater than n
        while miss <= n:

            if i < len(nums) and nums[i] <= miss:
                # Update miss using the current element in nums
                miss += nums[i]
                i += 1
            else:
                # Add miss to nums and increment patches
                # To maximize coverage, we choose to add miss itself to the array.
                # By doubling miss, we guarantee that we cover all numbers from miss to 2 * miss - 1.
                # This approach ensures that we efficiently expand the range of numbers we can form.

                # However, when the next number in nums is beyond the current reach (nums[i] > x),
                # we can't use it to expand our range and must add (patch) a new number.
                # The most efficient number to add is the next number just after the current reach (x itself),
                # which maximally extends the range by doubling it
                # (since before the patch we could reach x - 1, after adding x, we can reach 2x - 1).
                miss *= 2
                patches += 1

            # print(miss)

        return patches


# Example usage:
nums1 = []
n1 = 10
sol = Solution()

print(sol.minPatches(nums1, n1))

# nums2 = [1, 5, 10]
# n2 = 20
# print(sol.minPatches(nums2, n2))  # Output: 2

# nums3 = [1, 2, 2]
# n3 = 5
# print(sol.minPatches(nums3, n3))  # Output: 0
