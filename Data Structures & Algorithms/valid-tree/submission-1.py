class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) + 1 != n:
            return False
        
        mapping = defaultdict(list)
        for n1,n2 in edges:
            mapping[n1].append(n2)
            mapping[n2].append(n1)
        # connected
        # acyclic
        visited = set()
        found = 0
        def dfs(node):
            nonlocal found
            if node in visited:
                return
            visited.add(node)
            found+=1
            neighbors = mapping[node]
            for n in neighbors:
                dfs(n)
        dfs(0)
        return found == n

