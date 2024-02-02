class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        def makeSeqNum(start, length):
            num = ""
            for i in range(length):
                num += str(start + i)
            return int(num)
        
        output = []
        low_str = str(low)
        high_str = str(high)
        first_dig = int(low_str[0])
        places = len(low_str)
        
        while places <= len(high_str):
            while first_dig <= 10 - places:
                seq_num = makeSeqNum(first_dig, places)
                if low <= seq_num <= high:
                    output.append(seq_num)
                elif seq_num > high:
                    return output
                first_dig += 1
            places += 1
            first_dig = 1
        return output

s = Solution()
print(s.sequentialDigits(100, 300))
print(s.sequentialDigits(1000, 13000))
print(s.sequentialDigits(10, 1000000000))