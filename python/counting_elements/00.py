class Solution:
    def countElements(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
        
        odict = {}
        n = 0
        for i in range(len(arr)):
            if arr[i] not in odict:
                odict[arr[i]] = 1
            else:
                odict[arr[i]] += 1
            
        arr = set(arr)
        for j in arr:
            if j - 1 in odict:
                n += odict[j-1]
                
        return n

        
        ## Other way around !!
        #
        #arr = sorted(arr)
        #od = {k: 0 for k in arr}
        #n = 0
        #pntr = 1
        #for k in od:
        #    while pntr < len(arr) and arr[pntr] <= k + 1:
        #        if arr[pntr] == k + 1:
        #            n += 1
        #        pntr += 1
        #return n
    
