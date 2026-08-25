class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=max(nums)
        l=[]
        i=1
        s1=1
        while s+k>s1:
                s1=k*i
                l.append(s1)
                i+=1
        for i in l:
                if i not in nums:
                    return i