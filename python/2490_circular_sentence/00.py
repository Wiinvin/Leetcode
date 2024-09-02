class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        if len(sentence) < 2:
            return True

        first_char = sentence[0]
        running_ch = sentence[0]
        i = 1
        while i < len(sentence):
            if sentence[i] == " ":
                if running_ch != sentence[i+1]:
                    return False
                i += 1
            running_ch = sentence[i]
            i += 1

        if running_ch != first_char:
            return False

        return True
                
