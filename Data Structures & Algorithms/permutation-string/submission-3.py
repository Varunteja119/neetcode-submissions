class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        a=[0]*26
        b=[0]*26
        l=0
        for r in range(len(s1)):
            a[ord(s1[r])-ord('a')]+=1
            b[ord(s2[r])-ord('a')]+=1
        m=0
        for i in range(26):
            m+=(1 if a[i]==b[i] else 0)
        for r in range(len(s1),len(s2)):
            if m==26:
                return True
            ind=ord(s2[r])-ord('a')
            b[ind]+=1
            if a[ind]==b[ind]:
                m+=1
            elif a[ind]+1==b[ind]:
                m-=1
            ind=ord(s2[l])-ord('a')
            b[ind]-=1
            if a[ind]==b[ind]:
                m+=1
            elif a[ind]-1==b[ind]:
                m-=1
            l+=1
        return m==26

                 



             
