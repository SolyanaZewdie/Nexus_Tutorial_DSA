class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=len(s)-1
        res=[]

        while i >= 0:
            if s[i] == '#':
                n=int(s[i-2:i]) +96
                res.append(chr(n))
                i-=3
            else: 
                n=int(s[i])+96
                res.append(chr(n))
                i-=1
        r= reversed(res)       
        return "".join(r)
