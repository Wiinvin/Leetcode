class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """


        i = 0
        while sentence[i] == " ":
            i += 1

        word_count = -1

        while i < len(sentence):
            if sentence[i] == " ":
                i += 1
                continue
            if i and sentence[i-1] == " ":
                word_count += 1
    
            if (sentence[i-1] == " " or not i) and sentence[i] == searchWord[0]:
                j = 1
                i += 1
                while j < len(searchWord) and searchWord[j] == sentence[i]:
                    j += 1
                    i += 1
                if j == len(searchWord):
                    
                    return word_count + 2


            i += 1

        return -1
