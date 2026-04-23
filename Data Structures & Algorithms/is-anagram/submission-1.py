class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount={}
        tcount={}
        if(len(s) != len(t)):
            return False
            
        for i in range(len(s)):
            scount[s[i]]=0
            tcount[t[i]]=0

        for i in range(len(s)):
            if(s[i] in scount):
                scount[s[i]]+=1
            if(t[i] in tcount):
                tcount[t[i]]+=1

        for st in s:
            if(st in scount and st in tcount):
                if(scount[st] != tcount[st]):
                    return False
            else:
                return False
        return True



        
        
        