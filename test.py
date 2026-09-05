def combine(n, k):
    res = []

    def backtrack(curr, start, n):
        nonlocal res

        if len(curr) == k:
            res.append(curr[:])
            return

        for i in range(start, n):
            curr.append(i)
            backtrack(curr, i + 1, n)
            curr.pop()

    backtrack([], 1, n + 1)
    return res

print(combine(4, 2))

