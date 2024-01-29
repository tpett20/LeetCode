# 1694. Reformat Phone Number
# You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.
# You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes. Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits. The final digits are then grouped as follows:
    # 2 digits: A single block of length 2.
    # 3 digits: A single block of length 3.
    # 4 digits: Two blocks of length 2 each.
# The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks of length 1 and produce at most two blocks of length 2.
# Return the phone number after formatting.

class Solution:
    def reformatNumber(self, number: str) -> str:
        nums = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        digits = ""
        for num in number:
            if num in nums:
                digits += num
        remainder = len(digits) % 3
        if remainder == 0:
            final_nums = 3
        elif remainder == 1:
            final_nums = 4
        else:
            final_nums = 2
        output = ""
        for i in range(len(digits) - final_nums):
            output += digits[i]
            if (i + 1) % 3 == 0:
                output += "-"
        for i in range(len(digits) - final_nums, len(digits)):
            output += digits[i]
            if final_nums == 4 and len(digits) - i == 3:
                output += "-"
        return output

s = Solution()
print(s.reformatNumber("1-23-45 6"))
print(s.reformatNumber("123 4-567"))
print(s.reformatNumber("123 4-5678"))