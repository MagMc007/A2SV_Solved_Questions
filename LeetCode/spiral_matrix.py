# https://leetcode.com/problems/spiral-matrix/description/
# 54. Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 4 delimiters
        # these 4 keep converging per step
        top = 0
        left = 0
        bottom = len(matrix)
        right = len(matrix[0])

        output = []
        # iterators
        i = 0 # rows
        j = 0 # cols

        # we will be using while loop
        cells = (len(matrix) * len(matrix[0]))
        while len(output) < cells:
            top += 1
            # go right # moving cols
            # when you reach delimiter stop
            # converget your delimiter
            while j < right:
                output.append(matrix[i][j])
                j += 1
            i += 1
            right -= 1 
            j -= 1 # why ? cos we increased 1, idx out of bound

            # move down
            # rows
            while i < bottom:
                output.append(matrix[i][j])
                i += 1
            bottom -= 1
            i -= 1
            j -= 1


            # here we need to include a condition to break out
            if len(output) == cells:
                break

            # move left
            while j > left - 1:  # keep an eye out, goes ot of boud cos of -1
                output.append(matrix[i][j])
                j -= 1
            j += 1
            left += 1
            i -= 1

            # if len(output) == cells:
            #     break

            # move up
            while i > top - 1:
                output.append(matrix[i][j])
                i -= 1
            j += 1
            i += 1
            
        return output


