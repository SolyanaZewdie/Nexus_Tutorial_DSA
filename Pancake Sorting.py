class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(arr)
        
        for size in range(n, 1, -1):
            max_index = arr.index(max(arr[:size]))
            
            if max_index != size - 1:
                if max_index != 0:
                    res.append(max_index + 1)
                    arr[:max_index + 1] = reversed(arr[:max_index + 1])
                
                res.append(size)
                arr[:size] = reversed(arr[:size])
        
        return res
