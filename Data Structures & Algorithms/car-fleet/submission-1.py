class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pa = [(p, s) for p, s in zip(position, speed)]
        pa.sort(reverse=True)

        fleets = 1
        prevtime = (target - pa[0][0]) / pa[0][1]
        for i in range(1, len(pa)):
            currcar = pa[i]
            currtime = (target - currcar[0]) / currcar[1]
            if currtime > prevtime:
                fleets += 1
                prevtime = currtime
        return fleets        
            
                
