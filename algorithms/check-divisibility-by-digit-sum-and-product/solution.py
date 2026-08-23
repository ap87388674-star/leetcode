class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        import math
        sumodd=0
        sumeven=0       
        for i in range(1,2*n+1):
            if i%2==0:
                sumeven+=i
            else:
                sumodd+=i
        return math.gcd(sumodd,sumeven)


        

        