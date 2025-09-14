# 966. Vowel Spellchecker
# Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.
# For a given query word, the spell checker handles two categories of spelling mistakes:
# Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
    # Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
    # Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
    # Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
# Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
    # Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
    # Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
    # Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
# In addition, the spell checker operates under the following precedence rules:
    # When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
    # When the query matches a word up to capitlization, you should return the first such match in the wordlist.
    # When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
    # If the query has no matches in the wordlist, you should return the empty string.
# Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

from typing import List

class Solution:
    def replace_vowels(self, string: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        new_str = ""
        for char in string:
            new_str += "*" if char in vowels else char
        return new_str
    
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        answer = []
        exact_matches = set(wordlist)
        cap_options = {}
        vwl_options = {}
        for word in wordlist:
            lwr = word.lower()
            vwl_cleaned = self.replace_vowels(lwr)
            if lwr not in cap_options:
                cap_options[lwr] = word
            if vwl_cleaned not in vwl_options:
                vwl_options[vwl_cleaned] = word
        for q in queries:
            lwr = q.lower()
            vwl_cleaned = self.replace_vowels(lwr)
            if q in exact_matches:
                answer.append(q)
            elif lwr in cap_options:
                answer.append(cap_options[lwr])
            elif vwl_cleaned in vwl_options:
                answer.append(vwl_options[vwl_cleaned])
            else:
                answer.append("")
        return answer

s = Solution()
word_list = ["Mets", "mets"]
qs = ["mats", "mets", "METS", "Matz"]
print(s.spellchecker(word_list, qs))