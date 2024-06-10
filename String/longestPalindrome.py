class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)  # calculating size of s
        if n < 2:
            # if s is empty then size will be 0.
            # if n==1 then, answer will be 1(single character will always palindrome)
            return s

        start = 0
        maxLength = 1
        for i in range(n):
            # use each `i` as the center to expand to both sides
            # `low` to the left, `high` to the right
            low = i - 1
            high = i + 1
            # as long as the characters are same, keep moving the high pointer to the right
            while high < n and s[high] == s[i]:
                high = high + 1

            # as long as low and high are same, keep moving the low pointers to the left
            while low >= 0 and s[low] == s[i]:
                low = low - 1

            # as long as low and high are same, expand both pointer to left and right
            while low >= 0 and high < n and s[low] == s[high]:
                low = low - 1
                high = high + 1

            # the length of the palindrome s
            length = high - low - 1

            if maxLength < length:
                maxLength = length
                # store the start index of the palindrome s
                start = low + 1

        return s[start : start + maxLength]


if __name__ == "__main__":

    # Input: s = "babad"
    # Output: "bab"

    sol = Solution()
    res = sol.longestPalindrome("babadasdfasdfwerrwerfffffsdfsdfw2refdsfddfsdf")
    print(res)
