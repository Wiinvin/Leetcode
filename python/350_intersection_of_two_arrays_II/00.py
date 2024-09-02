from collections import defaultdict, Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_cntr1 = Counter(nums1)
        nums_cntr2 = Counter(nums2)

        cmmn_ks = set(nums_cntr1.keys()).intersection(set(nums_cntr2.keys()))
        cmmns = []
        for k in cmmn_ks:
            entries = []
            min_k = min(nums_cntr1[k], nums_cntr2[k])
            entries = [k] * min_k
            cmmns += entries

        return cmmns

