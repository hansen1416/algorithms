""""
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. 
You are given an integer array customers of length n where customers[i] is the number of the customer 
that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. 
You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16

Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.


Example 2:

Input: customers = [1], grumpy = [0], minutes = 1
Output: 1

"""

from typing import List


class Solution:

    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        """
        when use a slding window to calculate the change, usually don't need to iterate through the entire array,
        only need to keep track of the item out of the window, and the item newly added to the window

        1. becasue use the technique is always beneficial, so use it at the beginning of tne day, use it as a baseline
        2. keep a sliding window of size `minutes`
        3. `left_index` is the beginning of the previous window, `right_index` is the next index of the previous window
        4. when window moves, decrement the current_satisfied by customers[left_index] if grumpy[left_index] is 1,
            increment the current_satisfied by customers[right_index] if grumpy[right_index] is 1
        5. record the maximum satisfied customers
        """

        satisfied = 0
        # assume the use the technique at the beginning of the day, 0 - minutes
        for enter_time in range(len(customers)):
            if enter_time >= 0 and enter_time < minutes:
                satisfied += customers[enter_time]
            elif grumpy[enter_time] == 0:
                satisfied += customers[enter_time]

        max_satisfied = satisfied

        left_index = 0
        right_index = minutes

        while right_index < len(customers):
            # when window moves, decrement the current_satisfied by customers[left_index] if grumpy[left_index] is 1,
            if grumpy[left_index] == 1:
                satisfied -= customers[left_index]
            # increment the current_satisfied by customers[right_index] if grumpy[right_index] is 1
            if grumpy[right_index] == 1:
                satisfied += customers[right_index]

            if satisfied > max_satisfied:
                max_satisfied = satisfied
            # move the window
            left_index += 1
            right_index += 1

        return max_satisfied


if __name__ == "__main__":

    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    minutes = 3

    sol = Solution()

    print(sol.maxSatisfied(customers, grumpy, minutes))

    customers = [1]
    grumpy = [0]
    minutes = 1

    print(sol.maxSatisfied(customers, grumpy, minutes))
