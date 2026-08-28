class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        s= str(n)
        for i in sorted(s):
               l.append(int(i))
        return(l[-1]*l[-2])
               
