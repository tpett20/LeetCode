# 1408. String Matching in an Array
# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.
# A substring is a contiguous sequence of characters within a string

def stringMatching(words):
    def check_str(short, long):
        if len(short) == len(long):
            return False
        for i in range(len(long) - len(short) + 1):
            if short == long[i : i + len(short)]:
                return True
        return False

    output = []
    if len(words) == 1:
        return output
    words.sort(key=len)
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if check_str(words[i], words[j]):
                output.append(words[i])
                break
    return output

print(stringMatching(["mass","as","hero","superhero"]))
print(stringMatching(["leetcode","et","code","co"]))
print(stringMatching(["blue","green","bu"]))