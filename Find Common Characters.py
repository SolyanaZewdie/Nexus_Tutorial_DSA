class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common = [0] * 26
        for ch in words[0]:
            common[ord(ch) - ord('a')] += 1

        for word in words[1:]:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            for i in range(26):
                common[i] = min(common[i], count[i])

        res = []
        for i in range(26):
            res.extend([chr(i + ord('a'))] * common[i])

        return res
