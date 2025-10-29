class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        b = 0
        while (b + 1) * (b + 1) <= c:
            b += 1

        a = 0
        while a <= b:
            current = a * a + b * b
            if current == c:
                return True
            elif current < c:
                a += 1
            else:
                b -= 1
        return False
