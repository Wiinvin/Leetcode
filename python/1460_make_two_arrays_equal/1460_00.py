class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        
        for i in range(len(target)):
            stack = []
            for j in range(i, len(arr)):
                if arr[j] != target[i]:
                    stack.append(arr[j])
                else:
                    k = i + 1
                    arr[i] = arr[j]
                    while stack:
                        arr[k] = stack.pop()
                        k += 1
                    break

            if stack:
                return False
        print(arr)
        return True  
