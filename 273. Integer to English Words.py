def less1000(x, s):
    less20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    if x == 0:
        return ""
        
    if x < 20:
        ret = less20[x]
    elif x < 100:
        ret = tens[x/10] + " " + less20[x%10]
    else:
        ret = less20[x/100] + " Hundred " + less1000(x % 100, "")
    return ret.strip() + s
        
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        ans = ""
        for i, j in zip([10**9, 10**6, 10**3, 1], [" Billion", " Million", " Thousand", ""]):
            ans = (ans + " " + less1000(num / i % 1000, j)).strip()
        return ans
        