# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, target):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # This list a1 is passed as an argument
        # in treeToList method which is later
        # on filled by the values of BST
        arr1 = []

        # a2 list contains all the values of BST
        # returned by treeToList method
        arr2 = self.tree_to_list(root, arr1)

        # Starting index of a2
        start = 0

        # Ending index of a2
        end = len(arr2) - 1

        while start < end:

            # If target found
            if arr2[start] + arr2[end] == target:
                # print(f"Pair Found: {arr2[start]} + {arr2[end]} = {target}")
                return True

            # Decrements end
            if arr2[start] + arr2[end] > target:
                end -= 1

            # Increments start
            if arr2[start] + arr2[end] < target:
                start += 1

        # print("No such values are found!")
        return False

    # Function that adds values of given BST into
    # ArrayList and hence returns the ArrayList
    def tree_to_list(self, root, arr):

        if not root:
            return arr

        self.tree_to_list(root.left, arr)
        arr.append(root.val)
        self.tree_to_list(root.right, arr)

        return arr
