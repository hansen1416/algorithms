"""
You are given n projects where the ith project has a pure profit profits[i] 
and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, 
you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, 
and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.
"""

from typing import List
import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        """
        when it comes to the problem of maximizing/minimizing the value of a list of items,
        headq is a good choice to store the items, and get the max value
        """

        # Create a list of (capital, profit) pairs
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        # Sort the projects by capital in ascending order
        projects.sort(reverse=False)

        # Max heap to store profits of available projects
        max_heap = []

        # left of the project_idx is the projects that have been added to the heap
        project_idx = 0

        for _ in range(k):
            # Add projects with capital <= current capital to the max heap
            # we have to do this each time start a new project
            # use `project_idx` to avoid adding the same project multiple times
            for j in range(project_idx, len(profits)):
                # when the capital is less than the current capital, add the profit to the heap
                if projects[j][0] <= w:
                    heapq.heappush(max_heap, -projects[j][1])
                    project_idx = j + 1
                else:
                    break

            # If there are available projects, invest in the most profitable one
            if max_heap:
                w += -heapq.heappop(max_heap)
            else:
                break

        return w


if __name__ == "__main__":

    # Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
    # Output: 4
    # Explanation: Since your initial capital is 0, you can only start the project indexed 0.
    # After finishing it you will obtain profit 1 and your capital becomes 1.
    # With capital 1, you can either start the project indexed 1 or the project indexed 2.
    # Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
    # Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

    sol = Solution()

    res = sol.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1])
    print(res)

    # Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
    # Output: 6

    res = sol.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2])
    print(res)
