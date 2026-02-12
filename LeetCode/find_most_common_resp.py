# https://leetcode.com/problems/find-the-most-common-response/description/
# 3527. Find the Most Common Response
from collections import defaultdict
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        resp_cnt = defaultdict(int)

        for resp in responses:
            # change them to set to avoid those repeated
            resp_set = set(resp)
            for resp_ in resp_set:
                resp_cnt[resp_] += 1
        # not that we have the count of all responses
        # check and reurn the biggest count
        
        most_common = ["", 0]

        for key, value in resp_cnt.items():
            if value > most_common[1]:
                most_common = [key, value]
                # if equal take the lexicog_ smaller
            elif value == most_common[1]:
                most_common[0] = min(most_common[0], key)

        return most_common[0]


