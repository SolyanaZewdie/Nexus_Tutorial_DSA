class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        n = len(skill)
        S = sum(skill)
        team_num= n // 2

        if S % team_num != 0:
            return -1

        skill.sort()

        left=0
        right=n-1
        sums=0
        target = skill[left]+skill[right]

        while left<right:
            if skill[left+1]+skill[right-1]!=target:
                return -1
            sums +=skill[left]*skill[right]
            left+=1
            right-=1
        return sums

        
