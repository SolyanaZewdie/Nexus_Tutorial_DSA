class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n = len(piles) // 3
        result = 0

        for i in range(n, len(piles), 2):
            result += piles[i]

        return result
