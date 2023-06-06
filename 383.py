# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

def canConstruct(ransomNote, magazine):
    map = {}
    for char in magazine:
        if map.get(char): 
            map[char] += 1
        else: 
            map[char] = 1
    for char in ransomNote:
        if map.get(char):
            map[char] -= 1
        else: 
            return False
    return True

print(canConstruct('abb', 'aba'))