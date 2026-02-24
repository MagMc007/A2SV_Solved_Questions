# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/
# 2491. Divide Players Into Teams of Equal Skill
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # if it is odd, no way to pair 
        if len(skill) % 2:
            return -1
        
        # sorting the skills
        skill.sort()

        pairs = []
        # get the sum of the elements
        sum_ = skill[0] + skill[-1]

        # colliding pointers to group
        left = 0
        right = len(skill) - 1

        while left < right:
            curr_sum = skill[left] + skill[right]
            if curr_sum != sum_:
                return -1
            pairs.append((skill[left], skill[right]))
            right -= 1
            left += 1

        chemi = 0
        # calculate the chemistry
        for pair1, pair2 in pairs:
            chemi += pair1 * pair2

        return chemi


