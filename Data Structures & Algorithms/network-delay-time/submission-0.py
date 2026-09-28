class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for t in times:
            edges[t[0]].append((t[2],t[1]))


        heap = [(0,k)]
        visited = set()
        t = 0
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(w1,t)
            neighbors = edges[n1]
            for w2,n2 in neighbors:
                if n2 not in visited:
                    heapq.heappush(heap,(w1+w2,n2))
        
        for i in range(1,n+1):
            if i not in visited:
                return -1
            
        return t

