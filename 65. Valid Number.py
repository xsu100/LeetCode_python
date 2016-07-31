def isSignedInteger(s):
    if len(s) == 0:
        return False
    if s[0] in "+-":
        return isSignedInteger(s[1:])
    return isUnsignedInteger(s)
        
def isUnsignedInteger(s):
    if (set(s) <= set(string.digits)) == False:
        return False
    return len(s) != 0

def isSignedReal(s):
    if len(s) == 0:
        return False
    if s[0] in "+-":
        return isSignedReal(s[1:])
    return isUnsignedReal(s)
    
def isUnsignedReal(s):
    if not set(s) <= set(string.digits+"."):
        return False
    s = s.split(".")
    if len(s) > 2:
        return False
    if len(s) == 2:
        return isUnsignedInteger(s[0]) or isUnsignedInteger(s[1])
    return True
    
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip().split("e");
        if len(s) == 1:
            return isSignedReal(s[0])
        if len(s) == 2:
            return isSignedReal(s[0]) and isSignedInteger(s[1])
        return False

'''
An other tricky solution:

try:
    float(s)
except:
    return False
return True
'''

