# 2125. Number of Laser Beams in a Bank
# Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.
# There is one laser beam between any two security devices if both conditions are met:
# - The two devices are located on two different rows: r1 and r2, where r1 < r2.
# - For each row i where r1 < i < r2, there are no security devices in the ith row.
# Laser beams are independent, i.e., one beam does not interfere nor join with another.
# Return the total number of laser beams in the bank.

class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        def count_lasers(row):
            count = 0
            for cell in row:
                if cell == '1':
                    count += 1
            return count

        total = 0
        if len(bank) == 1:
            return total
        prev_sum = count_lasers(bank[0])
        for i in range(1, len(bank)):
            curr_sum = count_lasers(bank[i])
            if curr_sum > 0:
                total += (prev_sum * curr_sum)
                prev_sum = curr_sum
        return total

s = Solution()
print(s.numberOfBeams(["011001", "000000", "010100", "001000"]))
print(s.numberOfBeams(["000", "111", "000"]))