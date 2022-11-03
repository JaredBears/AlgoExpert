def findClosestValueInBst(tree, target):
    closestDistance = closestVal = float('inf')
    def helper(node):
        nonlocal closestDistance
        nonlocal closestVal
        if not node:
            return
        distance = abs(node.value - target)
        if distance < closestDistance:
            closestDistance = distance
            closestVal = node.value
        if node.value < target:
            helper(node.right)
        else:
            helper(node.left)
    helper(tree)
    return closestVal

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
