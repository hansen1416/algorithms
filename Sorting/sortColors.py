from typing import List

"""
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # intialize the pointers
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            # if the current element is 1 (white), move the white pointer
            if nums[white] == 1:
                white += 1
            elif nums[white] == 0:
                # swap the current element with the red pointer
                nums[red], nums[white] = nums[white], nums[red]
                # increment the red and white pointers
                red += 1
                white += 1
            else:
                # when the white pointer is at a 2 (blue)
                # swap the current element with the blue pointer
                # and decrement the blue pointer
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Input: nums = [2,0,1]
# Output: [0,1,2]

sol = Solution()
nums = [2, 0, 2, 1, 1, 0, 1, 2, 2, 1, 2, 0, 1, 1, 2, 1, 0, 0, 2, 1, 1, 0]
sol.sortColors(nums)

print(nums)
