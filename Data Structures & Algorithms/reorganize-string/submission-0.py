class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        n = len(s)
        if max(freq.values()) > (n + 1) // 2:
            return ""
        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)
        result = []
        while len(heap) >= 2:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)
            result.append(char1)
            result.append(char2)
            count1 += 1
            count2 += 1
            if count1 < 0:
                heapq.heappush(heap, (count1, char1))
            if count2 < 0:
                heapq.heappush(heap, (count2, char2))
        if heap:
            count, char = heapq.heappop(heap)
            result.append(char)
        return "".join(result)