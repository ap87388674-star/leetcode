class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s= str(n)
        l=[]
        for i in s:
            l.append(int(i))
        digit_sum=(sum(l))
        digit_product=1
        for i in l:
            digit_product=i* digit_product
        add= digit_sum+ digit_product
        if n%add==0:
            return True
        return False

