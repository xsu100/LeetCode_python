class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1]+nums+[1]
        n = len(nums)
        dp = [[0]*n for i in ' '*n]
        for start in range(n-2, 0, -1):
            for end in range(start, n-1):
                for k in range(start, end+1): #nums[k] is the last balloon in nums[start...end]
                    dp[start][end] = max(dp[start][end], dp[start][k-1] + dp[k+1][end] + nums[start-1] * nums[k] * nums[end+1])
        return dp[1][n-2]
