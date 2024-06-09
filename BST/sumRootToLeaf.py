# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root_to_leaf = 0
        stack = [(root, 0)]

        while stack:
            root, curr_number = stack.pop()
            if root is not None:
                # when reaching a level
                # curr_number is shifted left by one bit (using << 1)
                # and then the bitwise OR operation (|) is performed with the value of the current node (root.val).
                # This essentially creates a new number where the left bits (excluding the rightmost bit))
                # represent the values from previous nodes in the path,
                # and the rightmost bit represents the current node's value.
                curr_number = (curr_number << 1) | root.val

                if root.left is None and root.right is None:
                    # when reach a leaf, the curr_number is something like 101, we can just add it to `root_to_leaf`
                    root_to_leaf += curr_number
                else:
                    # when not a leaf, we continue to traverse the tree
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))

        return root_to_leaf


if __name__ == "__main__":

    from BST.utils import to_binary_tree

    root = [1, 0, 1, 0, 1, 0, 1]
    obj = Solution()

    print(obj.sumRootToLeaf(to_binary_tree(root)))
    # Output: 22
    # Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

    root = [0]
    print(obj.sumRootToLeaf(to_binary_tree(root)))
    # Output: 0
