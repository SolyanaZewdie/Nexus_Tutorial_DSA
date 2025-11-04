class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        summ = sum(nums[:k])
        max_ave=summ/float(k)
        n=len(nums)
        for i in range(k,n):
            summ += nums[i] - nums[i-k]
            max_ave=max(max_ave,summ/float(k))
        return max_ave
