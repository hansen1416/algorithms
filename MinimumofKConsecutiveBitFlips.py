"""
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, 
and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].
Example 2:

Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].
Example 3:

Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation: 
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]

"""

from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        length = len(nums)  # Length of the input array.
        flips = [0] * (length + 1)  # Differential array to track flips.
        total_flips = 0  # Total flips made so far.
        flip_counter = 0  # The aggregated flips affecting the current position.

        # Go through each number in the array.
        for index, val in enumerate(nums):
            flip_counter += flips[
                index
            ]  # Add current differential flips to the counter.

            # Check if we need to flip the current bit to 1.
            # If the sum of our counter and the value is even, that means it is 0 and we need to flip it.
            if (val + flip_counter) % 2 == 0:
                if (
                    index + k > length
                ):  # If flip would go beyond array, it's impossible.
                    return -1

                # We need to flip the current bit and the next k-1 bits.
                # Mark the beginning of flip.
                flips[index] += 1
                # Cancel out the flip after the k bits.
                flips[index + k] -= 1

                flip_counter += 1  # Account for the new flip in our counter.
                total_flips += 1  # Increment our total flips.

        return total_flips  # Return the total number of flips needed.


if __name__ == "__main__":

    sol = Solution()

    print(sol.minKBitFlips([0, 1, 0], 1))  # 2

    print(sol.minKBitFlips([1, 1, 0], 2))  # -1

    print(sol.minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3))  # 3
