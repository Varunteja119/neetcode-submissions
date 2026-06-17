class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=1+d.get(i,0)
        h=[]
        for i,n in d.items():
            heapq.heappush(h,[-n,i])
        a=[]
        while k>len(a):
            a.append(heapq.heappop(h)[1])
        return a
