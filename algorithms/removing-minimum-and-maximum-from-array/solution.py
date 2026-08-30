class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minimum= min(nums)
        maximum= max(nums)

        i = nums.index(minimum)
        j= nums.index(maximum)

        if i>j:
            i,j=j,i

        left = j+1
        n= len(nums)
        right= n-i
        both = (i+1) + (n-j)
        return min(left,right,both)