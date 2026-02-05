# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
# 599. Minimum Index Sum of Two Lists
class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        output = []
        min_sum = 2001

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    # check if the indices is a minimum sum
                    idx_sum = i + j

                    if idx_sum == min_sum:
                        # index sum equal to the existing words index sum
                        output.append(list1[i])
                    elif idx_sum < min_sum:
                        output = [list1[i]]
                        min_sum = idx_sum
        return output


"""
Better to use a hash map instead of newsting a forloop
"""
soln = Solution()
print(soln.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]))