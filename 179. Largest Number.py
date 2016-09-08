class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def comp(x, y):
            return 
        nums.sort(cmp = lambda x, y: cmp(str(y) + str(x), str(x) + str(y)))
        ans = reduce(lambda x, y: x * (10**(len(str(y)))) + y, nums)
        return str(ans)