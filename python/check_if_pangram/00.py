class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        chars = {ch for ch in sentence}
        return len(chars) == 26
