class Solution(object):
    def doNext(self, s):
        next = [0]
        for i in range(1, len(s)):
            j = next[i-1]
            while j and s[i] != s[j]:
                j = next[j-1]
            next.append(j + 1 if s[i] == s[j] else 0)
        return next
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            return s
        next = self.doNext(s + "#" + s[::-1])
        return s[next[-1]:][::-1] + s