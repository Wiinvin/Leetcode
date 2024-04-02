class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        #if len(matches) == 1:
        #    return [[matches[0][0]], [matches[0][1]]]

        counter_dict = defaultdict(int)
        for l, r in matches:
            counter_dict[r] += 1
        
        invincibles = set()
        runnerups = set()
        for l, r in matches:
            if l not in counter_dict:
                invincibles.add(l)
            if counter_dict[r] == 1:
                runnerups.add(r)

        return [sorted(list(invincibles)), sorted(list(runnerups))]   
