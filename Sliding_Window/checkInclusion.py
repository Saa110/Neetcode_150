class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d={}
        if len(s1)>len(s2):
            return False
        for i in s1:
            if d.get(i):
                d[i]+=1
            else:
                d[i]=1
        for i in range(len(s1)):
            if d.get(s2[i])!=None:
                d[s2[i]]-=1
            else:
                continue
        temp=list(d.values())
        if temp==[0]*len(d):
            return True
        for i in range(len(s1),len(s2)):
            l=i-len(s1)
            if d.get(s2[i])!=None:
                d[s2[i]]-=1
            if d.get(s2[l])!=None:
                d[s2[l]]+=1
            temp=list(d.values())
            print(temp)
            if temp==[0]*len(d):
                return True
        return False
            
        
