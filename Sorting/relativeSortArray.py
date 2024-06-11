from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # define a dictionary to store the frequency of each element in arr1
        freq = {}

        arr2_set = set(arr2)

        # define a list to store the elements in arr1 that are not in arr2
        # we will sort this list later
        not_in_arr2 = []

        # iterate through arr1 and store the frequency of each element in freq
        for num in arr1:

            if num not in arr2_set:
                # store the elements in arr1 that are not in arr2
                not_in_arr2.append(num)
            else:
                # store the frequency of the elements in arr1 that are in arr2
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1

        # iterate through arr2 and add the elements to the result list
        res = []

        for num in arr2:
            res.extend([num] * freq[num])

        # add the `not_in_arr2` list to the result list
        not_in_arr2.sort()

        res.extend(not_in_arr2)

        return res


# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]

# Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
# Output: [22,28,8,6,17,44]
