class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=''
        i=0
        j=0
        while i<len(word1) and j<len(word2):
            a+=word1[i]
            a+=word2[j]
            i+=1
            j+=1
        a+=word1[i:]
        a+=word2[j:]
        return a