class Solution:
    def minElement(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            l.append((str(i)))
        new=[]
        for j in l:
            new.append(list(j))
        new1=[]
        for k in new:
             new1.append(sum(int(x) for x in k))

        return min(new1)
            

            
        

        