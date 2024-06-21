"""
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. 
Rick has n empty baskets, the ith basket is at position[i], 
Morty has m balls and needs to distribute the balls into the baskets 
such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. 
The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.

Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.

"""

from typing import List


class Solution:

    def canDistributionMade(self, position: List[int], m: int, mid: int) -> bool:
        """
        check if `m` balls can be distributed at given `mid` days

        1. iterate through the position
        2. the distance between the left and right index are flowsers available at the given day
            `(right_index - left_index) // k` is the numbers of bouquets that can be made in this range
        """

        basket_count = 1
        last_position = position[0]

        for i in range(1, len(position)):
            if position[i] - last_position >= mid:
                # if the distance between the last position and the current position is geq to `mid`
                # then we can distribute the ball
                basket_count += 1
                last_position = position[i]
        # if the distributed ball is geq to `m` then return True
        return basket_count >= m

    def maxDistance(self, position: List[int], m: int) -> int:

        # do a binary search on the position array
        position.sort()

        left, right = 1, position[-1] - position[0]

        while left < right:

            mid = (left + right) // 2
            # check each `mid` distances if the `m` balls can be distributed
            if self.canDistributionMade(position, m, mid):
                left = mid + 1
            else:
                right = mid

        return left if self.canDistributionMade(position, m, left) else left - 1


if __name__ == "__main__":

    position = [1, 2, 3, 4, 7]
    m = 3

    s = Solution()
    print(s.maxDistance(position, m))

    position = [5, 4, 3, 2, 1, 1000000000]
    m = 2

    print(s.maxDistance(position, m))
