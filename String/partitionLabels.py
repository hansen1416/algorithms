"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Input: s = "eccbbbbdec"
Output: [10]

"""

from typing import List


class Solution(object):
    def partitionLabels(self, s: str) -> List[int]:
        # record the last occurrence of each character, {'a': 8, 'b': 5, 'c': 7, 'd': 14, ...}
        last = {c: i for i, c in enumerate(s)}
        # `j` is the highest of the last occurrence of all passed characters
        j = 0
        # `anchor` is the start of the current partition
        anchor = 0
        ans = []
        for i, c in enumerate(s):
            # record the highest of the last occurrence of all iterated characters
            # so that all char before char c will be in the same partition, (not occur after j)
            j = max(j, last[c])
            if i == j:
                # if i == j, means all char before i will not occur after i
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans


if __name__ == "__main__":

    s = "ababcbacadefegdehijhklij"

    sol = Solution()
    res = sol.partitionLabels(s)

    print(res)
