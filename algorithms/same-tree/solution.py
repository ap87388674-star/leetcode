class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        if max(d.values()) <3:
            return -1
        else:
            l1=[]
            a=None
            for key,value in d.items():
                if value>=3:
                    a= key
                l=[]
                for j  in range(len(nums)):
                    if nums[j]==a:
                        l.append(j)

                for i in range(len(l)-2):
                    score=(abs(l[i]-l[i+1])
                    + abs(l[i+1]- l[i+2])
                    + abs(l[i]-l[i+2]))
                    l1.append(score)
            return(min(l1))

        