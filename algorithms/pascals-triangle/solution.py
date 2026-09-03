class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l1=[[1]]
        
        for i in range(1,numRows):
            l2=[1]
            for j in range(i-1):
                l2.append(l1[i-1][j]+ l1[i-1][j+1])
            l2.append(1)    
            l1.append(l2)
        return l1