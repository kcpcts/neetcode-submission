class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        mapping = defaultdict(list)
        for n1,n2 in edges:
            mapping[n1].append(n2)
            mapping[n2].append(n1)
        
        left = set()
        
        for i in range(n):
            left.add(i)

        # dfs from some node
        # mark all reached as visited, remove from left
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            left.discard(node)
            neighbors = mapping[node]
            for n in neighbors:
                dfs(n)
        sol = 0
        while left:
            element = next(iter(left),None)
            dfs(element)
            sol+=1
            

        return sol

