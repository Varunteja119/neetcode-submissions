class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = sorted(
            (enqueue, process, i) for i, (enqueue, process) in enumerate(tasks))
        min_heap = []
        result = []
        time = 0
        i = 0
        n = len(tasks)
        while i < n or min_heap:
            if not min_heap and i < n and time < sorted_tasks[i][0]:
                time = sorted_tasks[i][0]
            while i < n and sorted_tasks[i][0] <= time:
                enqueue, process, index = sorted_tasks[i]
                heapq.heappush(min_heap, (process, index))
                i += 1
            process, index = heapq.heappop(min_heap)
            result.append(index)
            time += process
        return result