class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge = []
    
        while word1 or word2:
            if word1 > word2:
                merge.append(word1[0])
                word1 = word1[1:]
            else:
                merge.append(word2[0])
                word2 = word2[1:]
    
        return "".join(merge)
