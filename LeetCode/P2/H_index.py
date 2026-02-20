# https://leetcode.com/problems/h-index/description/
# 274. H-Index
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # The h-index is the largest number h such that a researcher 
        # has at least h papers, and each of those papers has
        # received h or more citations.
        
        # sorting in DESC order
        # obvious that the PRED papers have recieved ASC number of citations
        citations.sort(reverse=True)

        h = 0

        # get the point where the it cannot recieve h number of citations
        for i in range(len(citations)):
            # i + 1 the number of papers
            if citations[i] >= i + 1:
                h = i + 1

        return h