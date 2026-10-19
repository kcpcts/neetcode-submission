class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n <= 1:
            return n
        adjacency_list = defaultdict(list)
        for start,end in edges:
            adjacency_list[start].append(end)
            adjacency_list[end].append(start)
        
        # visited set
        # bfs on a non visited node until all nodes are visited
        # add 1 on bfs termination (explored entire connected component)
        remaining = set()
        for i in range(n):
            remaining.add(i)
        queue = deque()


        # not in remaining = visited
        # if we have remaining then there is another component yet to be explored
        count = 0
        while remaining:
            start = remaining.pop()
            queue = deque([start])
            while queue:
                current = queue.popleft()
                neighbors = [n for n in adjacency_list[current] if n in remaining]
                for n in neighbors:
                    remaining.remove(n)
                    queue.append(n)
            count += 1
        
        return count


