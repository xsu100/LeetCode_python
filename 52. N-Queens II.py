class Solution(object):
    def dfs(self, n, idx, col, diag, cdiag):
        if idx == n:
            return 1
        ans = 0
        mask = col | diag | cdiag
        for i in range(n):
            if mask & (1 << i) == 0:
                ans += self.dfs(n, idx+1, col | (1<<i), (diag | (1<<i)) << 1, (cdiag | (1<<i)) >> 1)
        return ans
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dfs(n, 0, 0, 0, 0)
