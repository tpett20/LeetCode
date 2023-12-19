# 661. Image Smoother
# An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells. If one or more of the surrounding cells of a cell is not present, we do not consider it in the average.
# Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        output = []
        for i in range(len(img)):
            sum = img[i][0]
            count = 1
            top = False
            btm = False
            if i > 0:
                sum += img[i - 1][0]
                count += 1
                top = True
            if i + 1 < len(img):
                sum += img[i + 1][0]
                count += 1
                btm = True
            output.append([])
            for j in range(len(img[i])):
                if j > 1:
                    sum -= img[i][j - 2]
                    count -= 1
                    if top:
                        sum -= img[i - 1][j - 2]
                        count -= 1
                    if btm:
                        sum -= img[i + 1][j - 2]
                        count -= 1
                if j + 1 < len(img[i]):
                    sum += img[i][j + 1]
                    count += 1
                    if top:
                        sum += img[i - 1][j + 1]
                        count += 1
                    if btm:
                        sum += img[i + 1][j + 1]
                        count += 1
                output[i].append(sum // count)
        return output

s = Solution()
print(s.imageSmoother([[100,200,100], [200,50,200], [100,200,100]]))