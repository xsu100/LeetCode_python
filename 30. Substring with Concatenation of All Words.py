class Solution(object):
    def gao(self, s, start, d, n, m):
        '''
        type s: str
        type start: int
        type d: dict
        '''
        ret =[]
        if (start + n * m > len(s)):
            return ret

        d2 = {}
        for j in range(start, start + n * m, n):
            d2[s[j : j+n]] = d2.get(s[j : j+n], 0) + 1

        for i in xrange(start, len(s) - n * m + 1, n):
            if set(d.items()).issubset(d2.items()):
                ret.append(i)
            ss = s[i : i+n]
            d2[ss] = d2.get(ss, 0) - 1
            ss = s[i+n*m : i+n*(m+1)]
            d2[ss] = d2.get(ss, 0) + 1
        return ret


    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        n, m = len(words[0]), len(words)
        d = {}
        for w in words:
            d[w] = d.get(w, 0) + 1
        for i in range(n):
            res += self.gao(s, i, d, n, m)
        return res
