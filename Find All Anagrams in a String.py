from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        target = Counter(p)
        window = Counter(s[:len(p)])
        answer = []

        if window == target:
            answer.append(0)

        for i in range(len(p), len(s)):
            left_char = s[i - len(p)]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]  
            right_char = s[i]
            window[right_char] += 1

            if window == target:
                answer.append(i - len(p) + 1)

        return answer
