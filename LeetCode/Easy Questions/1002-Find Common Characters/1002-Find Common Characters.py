from collections import Counter
from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_chars = Counter(words[0])
        for i in range(1, len(words)):
            # & is the intersection of the two counters 
            # (i.e., if a char appears twice in one word and once in another, value for that char is 1.)
            common_chars = common_chars & Counter(words[i])
        return sorted(common_chars.elements())

        