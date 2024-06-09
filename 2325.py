# 2325. Decode the Message
# You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:
    # 1. Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
    # 2. Align the substitution table with the regular English alphabet.
    # 3. Each letter in message is then substituted using the table.
    # 4. Spaces ' ' are transformed to themselves.
# For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
# Return the decoded message.

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        conv = ["_"] * 26
        ltr_code = 97
        for char in key:
            if char != " ":
                code = ord(char) - 97
                if conv[code] == "_":
                    conv[code] = chr(ltr_code)
                    ltr_code += 1
        msg_words = message.split(" ")
        output = []
        for word in msg_words:
            new_word = ""
            for char in word:
                code = ord(char) - 97
                new_word += conv[code]
            output.append(new_word)
        return " ".join(output)

s = Solution()
print(s.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
print(s.decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))