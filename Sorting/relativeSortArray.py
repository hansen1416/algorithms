# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]


def relative_sort(arr1, arr2):

    # define a dictionary to store the frequency of each element in arr1
    freq = {}

    # iterate through arr1 and store the frequency of each element in freq
    for num in arr1:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # define a list to store the elements in arr1 that are not in arr2
    # we will sort this list later
    not_in_arr2 = []

    # iterate through arr2 and add the elements to the result list
    res = []

    for num in arr2:
        res.extend([num] * freq[num])

    # add the not
