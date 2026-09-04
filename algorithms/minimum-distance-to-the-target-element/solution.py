class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        a=float(inf)
        for i in range(len(nums)):
            if nums[i]==target:
                if a> abs(i-start):
                    a= abs(i-start)
        return a    