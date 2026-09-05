def generate(numRows):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    dp = [[1] * i for i in range(numRows + 1)]
    for i in range(3, numRows + 1):
        for k in range(1, i - 1):
            dp[i][k] = dp[i - 1][k] + dp[i - 1][k - 1]
    return dp

generate(5)
