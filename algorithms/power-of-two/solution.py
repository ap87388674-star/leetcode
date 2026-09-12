class Solution:
    def convertToBase7(self, num: int) -> str:
        s=""
        negative=num<0
        num=abs(num)
    
        while (num)>=7:
            
            a= num//7
            num =num%7
            s+=str(num)
            num=a
        

        if negative:
            return "-"+ str(num)+ s[::-1]
        return str(num) + s[::-1]




        