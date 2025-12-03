def findpositive(st):
    for i in range(len(st)):
        if st[i]>=0:
            return i
    else :
        return 0
def findnegative(st):
    for i in range(len(st)):
        if st[i]<0:
            return i
    else :
        return 0
def reposition_number(orignal,final,s):
    s=s[:final]+[s[orignal]]+s[final:orignal]+s[orignal+1:]
    return s
def mix_numbers(s):
    
        
    r=0
    # for i in range(len(s)):
    #     if s[i]<0:
    #         s=s[0:r]+[s[i]]+s[r:i]+s[i+1:len(s)]
    #         r=3
    for k in range(len(s)-1):
        if k%2==0:
            if s[k]>=0:
                pass
            else:
                r=k
                i=k+ findpositive(s[k:])
                s=reposition_number(i,r,s)
        else:
            if s[k]<0:
                pass
            else:
                r=k
                i=k+findnegative(s[k:])
                s=reposition_number(i,r,s)
                
                
    return(s)
print( reposition_number(2,1,[1, 2, 3, -4, -1, 4]))
print("Answer=",mix_numbers([1, 2, 3, -4, -1, 4]))

print("Answer=",mix_numbers([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]))
        
        
        
