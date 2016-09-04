class Solution(object):
    def dfs(self, idx, s, wordDict, dp):
        if idx == len(s):
            return [[]]
        if idx in dp:
            return dp[idx]
        ans = []
        for i in xrange(idx, len(s)):
            if s[idx:i+1] in wordDict:
                ans += map(lambda x: x + [s[idx:i+1]], self.dfs(i+1, s, wordDict, dp))
        dp[idx] = ans
        return ans
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return map(lambda x: " ".join(x[::-1]), self.dfs(0, s, wordDict, {}))
