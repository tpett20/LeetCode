# 799. Champagne Tower
# We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.
# Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)
# For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.
# Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0
        prev_row = [[1, poured - 1]]
        for _ in range(query_row):
            new_row = []
            for i in range(len(prev_row) + 1):
                flow = 0
                if i - 1 >= 0:
                    flow += prev_row[i - 1][1] / 2
                if i < len(prev_row):
                    flow += prev_row[i][1] / 2
                if flow > 1:
                    fill = 1
                    overflow = flow - 1
                else:
                    fill = flow
                    overflow = 0
                new_row.append([fill, overflow])
            prev_row = new_row
        return prev_row[query_glass][0]

s = Solution()
print(s.champagneTower(5, 2, 0))
print(s.champagneTower(5, 2, 1))
print(s.champagneTower(5, 2, 0))