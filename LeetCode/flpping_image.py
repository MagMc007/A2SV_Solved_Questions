# https://leetcode.com/problems/flipping-an-image/description/
# 832. Flipping an Image
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        for i in range(rows):
            image[i] = image[i][::-1]
            for j in range(cols):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        return image
