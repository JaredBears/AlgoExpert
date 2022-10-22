# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    answers = []
    def helper(node, sum):
        if not node:
            return
        if not node.left and not node.right:
            answers.append(sum + node.value)
            return
        helper(node.left, sum + node.value)
        helper(node.right, sum + node.value)
    helper(root, 0)
    return answers
