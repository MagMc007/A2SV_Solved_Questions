# https://leetcode.com/problems/diagonal-traverse/description/
# 498. Diagonal Traverse

class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        # edges of the matrix i must watch
        top = 0
        left = 0
        right = len(mat[0])
        bottom = len(mat)

        output = []

        cells = len(mat) * len(mat[0])

        # instanciate iterators
        i = 0
        j = 0

        while len(output) < cells:
            # every traversal has a step where u head up
            # and down

            # go up
            # has_diagonal = (i) < top and (j) < right 
            
            while i >= top and j < right:
                output.append(mat[i][j])
                i -= 1
                j += 1

            # restore the values for the next iteration of going down
            if i < top and j >= right:  # both were out of bound
                i += 2
                j -= 1
            elif i < top:  # if only i was out of bound
                i += 1
            elif j >= right:  # only j exceeding
                j -= 1   # bring j back
                i += 2  # go one down 
            
            if len(output) == cells:
                break

            # go down

            # has_diagonal = i < bottom and j >= left
            while i < bottom and j >= left:
                output.append(mat[i][j])
                i += 1
                j -= 1

            # restore the values for the next iteration of going up
            if i >= bottom and j < left:  # both were out of bound
                j += 2
                i -= 1
            elif i >= bottom:  # if only i was out of bound
                i -= 1
                j += 2
            elif j < left:  # only j exceeding
                j += 1   # bring j back

        return output
                
soln = Solution()
print(soln.findDiagonalOrder([[2]]))
