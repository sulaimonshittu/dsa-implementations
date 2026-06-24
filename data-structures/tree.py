class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Tree(4)
intltr = Tree(2)
intrtr = Tree(5)
root.left = intltr
root.right = intrtr
intltr.left = Tree(1)
intltr.right = Tree(3)
intrtr.left = Tree(6)
intrtr.right = Tree(7)

def dfs(tree):
    if tree is None:
        return
    print(tree.val)
    dfs(tree.left)
    dfs(tree.right)

dfs(root)

