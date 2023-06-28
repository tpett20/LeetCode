# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

def mergeAlternately(word1, word2):
    word3 = ''
    i = 0
    while i < len(word1) and i < len(word2):
        word3 += word1[i] + word2[i]
        i += 1
    if i < len(word1):
        word3 += word1[i:len(word1)]
    elif i < len(word2):
        word3 += word2[i:len(word2)]
    return word3

print(mergeAlternately('a', 'bcd'))