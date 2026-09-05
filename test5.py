class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

def sumRootToLeaf(root):
    ans = 0

    def dfs(root, value):
        nonlocal ans
        if root.left is None and root.right is None:
            value = f"{value}{root.val}"
            ans += int(value, 2)
            return
        value = f"{value}{root.val}"
        if root.left:
            dfs(root.left, value)
            value = value[:-1]
        if root.right:
            dfs(root.right, value)
            value = value[:-1]

    dfs(root, "")
    return ans

sumRootToLeaf(root)