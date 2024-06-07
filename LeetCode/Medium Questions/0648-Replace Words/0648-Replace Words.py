from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        output = ""
        word_set = set(dictionary)
        for word in sentence.split():
            word_added = False
            for i in range(1, len(word)):
                if word[:i] in word_set:
                    output += word[:i] + " "
                    word_added = True
                    break
            if word_added == False:
                output += word + " "
        return output[:-1]