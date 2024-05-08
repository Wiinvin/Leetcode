class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        st = 1
        minvar = min([a, b])
        maxvar = max([a, b])
        lim = minvar // 2
        minvar_fact = set()
        while st <= lim:
            if minvar % st == 0 and maxvar % st == 0:
                minvar_fact.add(st)
            st += 1
        if maxvar % minvar == 0:
            minvar_fact.add(minvar)
        
        return len(minvar_fact)
