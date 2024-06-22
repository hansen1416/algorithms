"""
Given an array of integers nums and an integer k. 
A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
"""

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """ """
        res = 0
        i = 0
        count = 0
        n = len(nums)

        for j in range(n):
            # count the number of odd numbers between i and j
            # if k reaches 0, means we have found a subarray with k odd numbers
            # and reset the count, otherwise, keep the count as is,
            # since adding more even number to the right, does not change the number of odd numbers in subarray
            # and start inner loop
            if nums[j] % 2 == 1:
                k -= 1
                count = 0

            # the inner loop
            # shift i to the right as long as k is 0 (still k odd number between i and j)
            # and count += 1
            while k == 0:
                k += nums[i] & 1
                count += 1
                i += 1

            # add the count to the result,
            # both when add even number to the right, or remove even number from the left
            res += count

        return res


if __name__ == "__main__":
    nums1 = [1, 1, 2, 1, 1]
    k1 = 3
    sol = Solution()
    print(sol.numberOfSubarrays(nums1, k1))  # Output: 2

    nums2 = [2, 4, 6]
    k2 = 1
    print(sol.numberOfSubarrays(nums2, k2))  # Output: 0

    nums3 = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k3 = 2
    print(sol.numberOfSubarrays(nums3, k3))  # Output: 16
