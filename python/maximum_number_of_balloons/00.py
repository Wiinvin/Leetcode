class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        trgt_str = ["b", "a", "l", "l", "o", "o", "n"]
        trgt_dict = defaultdict(int)
        for k in trgt_str:
            trgt_dict[k] += 1
        
        indict = defaultdict(int)
        for k in text:
            indict[k] += 1
        
        den = []
        for k in trgt_str:
            den.append(indict[k] // trgt_dict[k])
        
        
        return min(den)
