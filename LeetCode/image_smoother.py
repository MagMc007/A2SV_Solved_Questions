# https://leetcode.com/problems/image-smoother/description/
# 661. Image Smoother

class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        # there are boundaries, must no be passed when looking for the 
        # 8 surrounding numbers
        top = 0
        left = 0
        bottom = len(img) - 1
        right = len(img[0]) - 1

        output = [[0] * len(img[0]) for _ in range(len(img))] 
        
        # iterate over each element and average the 8
        for i in range(len(img)):
            for j in range(len(img[0])):
                sum_ = img[i][j]
                count = 1

                # truth values
                has_left = j - 1 >= left
                has_right = j + 1 <= right
                has_top = i - 1 >= top
                has_bottom = i + 1 <= bottom

                # for the two elements beside it
                if has_left:
                    sum_ += img[i][j-1]
                    count += 1
                
                if has_right:
                    sum_ += img[i][j + 1]
                    count += 1
                
                # for those above it 
                if has_top:
                    sum_ += img[i - 1][j]
                    count += 1
                    if has_left:
                        sum_ += img[i - 1][j - 1]
                        count += 1
                    if has_right:
                        sum_ += img[i - 1][j + 1]
                        count += 1

                # for those below it
                if has_bottom:
                    sum_ += img[i + 1][j]
                    count += 1
                    if has_left:
                        sum_ += img[i + 1][j - 1]
                        count += 1
                    if has_right:
                        sum_ += img[i + 1][j + 1]
                        count += 1
                        
                output[i][j] = sum_ // count
                print(output[i][j])

        return output

soln = Solution()
print(soln.imageSmoother(img = [[1,1,1],[1,0,1],[1,1,1]]))

