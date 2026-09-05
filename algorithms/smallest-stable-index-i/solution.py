class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n= len(nums)
        max_value= float('inf')
        score= float('inf')
        min_value= float('-inf')
        for i in range(n):
            max_value= max(nums[0:i+1])
            min_value= min(nums[i: n])
            score= max_value-min_value
            if score<=k:
                return i
        return -1


    