class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        len2 = len(str2)
        # because always keep the longer string in str1, so when str2 is empty
        # it means it has been truncated to the end, so we can return str1
        if len2 == 0:
            return str1

        # always keep the longer string in str1
        if len(str1) < len2:
            return self.gcdOfStrings(str2, str1)

        # if str1 not start with str2, means gcd not exist
        if str1[:len2] != str2:
            return ""


# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
