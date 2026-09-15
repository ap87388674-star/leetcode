class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d=set(word)
        count=0
        
        for i in d:
            if i.islower() and i.upper() in d:
                count+=1
        return count
                


                

        