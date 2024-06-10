from typing import List
import heapq


class Solution(object):
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for p in points:
            heapq.heappush(min_heap, (p[0] ** 2 + p[1] ** 2, p[0], p[1]))

        i = 0
        res = []

        while i < k:
            _, x, y = heapq.heappop(min_heap)
            res.append([x, y])

            i += 1

        return res


if __name__ == "__main__":

    # Input: points = [[1,3],[-2,2]], k = 1
    # Output: [[-2,2]]
    sol = Solution()
    res = sol.kClosest([[1, 3], [-2, 2]], 1)
    print(res)
