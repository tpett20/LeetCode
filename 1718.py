# 1718. Construct the Lexicographically Largest Valid Sequence
# Given an integer n, find a sequence that satisfies all of the following:
# The integer 1 occurs once in the sequence.
# Each integer between 2 and n occurs twice in the sequence.
# For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
# The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.
# Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.
# A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def find_sequence(seq: List[int], rem: List[int], idx: int) -> List[int]:
            if not rem:
                return seq
            if idx >= len(seq):
                return False
            if seq[idx]:
                return find_sequence(seq.copy(), rem.copy(), idx + 1)
            for i in range(len(rem)):
                s = seq.copy()
                r = rem.copy()
                num = r.pop(i)
                s[idx] = num
                if num == 1 or (idx + num < len(seq) and s[idx + num] == 0):
                    if num != 1:
                        s[idx + num] = num
                    valid = find_sequence(s, r, idx + 1)
                    if valid:
                        return valid
            return False
        
        nums = []
        for i in range(n, 0, -1):
            nums.append(i)
        sequence = [0] * (n * 2 - 1)
        return find_sequence(sequence, nums, 0)

s = Solution()
print(s.constructDistancedSequence(2))
print(s.constructDistancedSequence(20))