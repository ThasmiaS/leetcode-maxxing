class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap --> O(n)
        map = {}
        
        for i,n in enumerate(nums):
            complement = target - n #target = n + complement
            if complement in map:
                return [map[complement], i]
            map[n] = i
        
        #BRUTE FORCE - O(n^2)
        '''indices = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                   return [i,j]'''