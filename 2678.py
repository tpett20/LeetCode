# 2678. Number of Senior Citizens
# You are given a 0-indexed array of strings details. Each element of details provides information about a given passenger compressed into a string of length 15. The system is such that:
    # The first ten characters consist of the phone number of passengers.
    # The next character denotes the gender of the person.
    # The following two characters are used to indicate the age of the person.
    # The last two characters determine the seat allotted to that person.
# Return the number of passengers who are strictly more than 60 years old.

from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                count += 1
        return count

s = Solution()
print(s.countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))