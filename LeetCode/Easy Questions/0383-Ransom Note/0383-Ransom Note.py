from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterCounts = defaultdict(int)
        for letter in magazine:
            letterCounts[letter] += 1
        for letter in ransomNote:
            if letterCounts[letter]:
                letterCounts[letter] -= 1
            else:
                return False
        return True