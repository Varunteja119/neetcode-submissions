class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        r=[]
        c=[]
        def back(s,re):
            if re==0:
                r.append(c.copy())
                return
            for i in range(s,len(candidates)):
                if candidates[i]>re:
                    break
                if i>s and candidates[i]==candidates[i-1]:
                    continue
                c.append(candidates[i])
                back(i+1,re-candidates[i])
                c.pop()
        back(0,target)
        return r