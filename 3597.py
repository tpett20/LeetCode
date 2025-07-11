# 3597. Partition String 
# Given a string s, partition it into unique segments according to the following procedure:
# Start building a segment beginning at index 0.
# Continue extending the current segment character by character until the current segment has not been seen before.
# Once the segment is unique, add it to your list of segments, mark it as seen, and begin a new segment from the next index.
# Repeat until you reach the end of s.
# Return an array of strings segments, where segments[i] is the ith segment created.

from typing import List

class Solution:
    def partitionString(self, s: str) -> List[str]:
        segments = []
        seen = set()
        seg = ""
        for char in s:
            seg += char
            if seg not in seen:
                seen.add(seg)
                segments.append(seg)
                seg = ""
        return segments

s = Solution()
print(s.partitionString("abbccccd"))