class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        j=1
        check=True
        for i in range(len(nums1)-1):
            if nums1[i]%2==0:
                if (nums1[i]- nums1[j])%2==0:
                    j+=1
                    pass
            elif nums1[i]%2!=0:
                if (nums1[i]- nums1[j])%2!=0:
                    j+=1
                    pass
            else:
                check=False
        if check :
            return True
        return False