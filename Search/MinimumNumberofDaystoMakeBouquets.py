"""
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. 
If it is impossible to make m bouquets return -1.

Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. 
We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.

Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. 
We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.

"""

from typing import List


class Solution:

    def canBouquetsMade(self, bloomDay: List[int], m: int, k: int, mid: int) -> bool:
        """
        check if `m` bouquets can be made at given `mid` days

        1. iterate through the bloomDay
        2. the distance between the left and right index are flowsers available at the given day
            `(right_index - left_index) // k` is the numbers of bouquets that can be made in this range
        """

        bouquet_count = 0

        left_index = 0
        right_index = 0

        for i in range(len(bloomDay)):
            if bloomDay[i] <= mid:
                # keep increasing the right index when the flower is available at `mid`
                right_index += 1
            else:
                # encounter a flower not available at `mid`
                # count the number of bouquets that can be made in this range
                bouquet_count += (right_index - left_index) // k
                # reset the left and right index to the current index
                left_index = i
                right_index = i
        # check the last range, because the loop ends before checking the last range
        bouquet_count += (right_index - left_index) // k
        # if the number of bouquets made is greater than or equal to `m`, return True
        return bouquet_count >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        left = min(bloomDay)
        right = max(bloomDay)

        # do a binary search between min day and max day in the `bloomDay`
        while left < right:
            mid = (left + right) // 2
            # check if `m` bouquets can be made at given `mid` days
            if self.canBouquetsMade(bloomDay, m, k, mid):
                # if True, then the right boundary can be reduced
                right = mid
            else:
                # if False, then the left boundary can be increased
                left = mid + 1

        # do a last check the `left` boundary, in the case of `left` kept increasing until reach the `right`
        return left if self.canBouquetsMade(bloomDay, m, k, left) else -1


if __name__ == "__main__":

    sol = Solution()

    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1

    res = sol.minDays(bloomDay, m, k)

    print(res)

    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 2

    res = sol.minDays(bloomDay, m, k)

    print(res)

    bloomDay = [7, 7, 7, 7, 12, 7, 7]
    m = 2
    k = 3

    res = sol.minDays(bloomDay, m, k)

    print(res)
