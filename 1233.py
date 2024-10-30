# 1233. Remove Sub-Folders from the Filesystem
# Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.
# If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".
# The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.
    # For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.

from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ref = set(folder)
        output = []
        for f in folder:
            parts = f[1:].split("/")
            trail = ""
            is_sub = False
            for i in range(len(parts) - 1):
                part = parts[i]
                trail += "/" + part
                if trail in ref:
                    is_sub = True
                    break
            if not is_sub:
                output.append(f)
        return output
    
s = Solution()
print(s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))