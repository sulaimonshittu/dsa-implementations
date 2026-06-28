from collections import deque

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

## pre-order traversal
def pdfs(tree):
    if tree is None:
        return
    print(tree.val)
    pdfs(tree.left)
    pdfs(tree.right)

pdfs(root)
print()

## in-order traversal
def idfs(tree):
    if tree is None:
        return
    idfs(tree.left)
    print(tree.val)
    idfs(tree.right)

idfs(root)
print()

## post-order traversal
def podfs(tree):
    if tree is None:
        return
    podfs(tree.left)
    podfs(tree.right)
    print(tree.val)

podfs(root)
print()

## bread-first search
def bfs(tree):
    if tree is None:
        return
    queue = deque([tree])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

bfs(root)

