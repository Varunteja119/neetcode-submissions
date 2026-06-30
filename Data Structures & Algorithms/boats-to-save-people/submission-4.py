class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        b=0
        people.sort()
        l=0
        r=len(people)-1
        while l<=r:
            if (people[l]+people[r])<=limit:
                b+=1
                l+=1
                r-=1
            elif people[l]>=limit:
                b+=1
                l+=1
            elif people[r]>=limit:
                b+=1
                r-=1
            else:
                b+=1
                r-=1
        return b 
