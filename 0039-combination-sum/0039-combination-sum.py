class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(remaining, start, combination):
            if remaining == 0:
                result.append(list(combination))
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                combination.append(candidate)
                backtrack(remaining - candidate, i, combination)
                combination.pop()
        
        backtrack(target, 0, [])
        return result
        