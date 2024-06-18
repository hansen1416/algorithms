"""
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.


Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
Example 2:

Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0


"""

from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        """
        1. sort the jobs by difficulty
        2. sort the workers by their ability
        3. for each worker, find the maximum profit that can be achieved by their ability,
            because the worker is sorted, higher ability worker can at least do the same job as the lower ability worker
            so only consider the jobs with higher difficulty than iterated jobs
        4. update the maximum profit
        """

        # create a list of tuples where each tuple contains the difficulty and profit
        jobs = list(zip(difficulty, profit))
        # sort the jobs by difficulty
        jobs.sort()

        # sort the workers by their ability
        worker.sort()
        # initialize the maximum profit to 0
        max_profit = 0
        # initialize the current max profit to 0
        # can not put this inside the loop, because we need to keep track of the maximum profit
        # it's possible that higher difficulty jobs have lower profit
        curr_max_profit = 0
        # initialize the job index to 0
        # monotonically increasing, because the worker is sorted,
        # higher ability worker can at least do the same job as the lower ability worker
        job_index = 0

        for ability in worker:
            # iterate through the jobs
            while job_index < len(jobs) and ability >= jobs[job_index][0]:
                # update the current max profit
                curr_max_profit = max(curr_max_profit, jobs[job_index][1])
                job_index += 1
            # update the maximum profit
            max_profit += curr_max_profit

        return max_profit


if __name__ == "__main__":

    sol = Solution()
    res = sol.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7])

    print(res)
