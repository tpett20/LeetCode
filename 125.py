# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
    import re
    s = re.sub('\W|_', '', s).lower()
    if s == s[::-1]:
        return True
    else: return False
    
print(isPalindrome('A man, a plan, a c_anal: Panama'))