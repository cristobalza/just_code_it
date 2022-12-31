class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.n = len(graph)
        self.g = {node: [] for node in range(self.n)}
        for node, e in enumerate(graph):
            self.g[node].extend(e)
        
        print(self.g)
        self.res = []
        self.backtrack(0, [0])
        return self.res
    
    def backtrack(self, node, subset):
        # solution
        if not self.g[node]:
            if node == self.n -1 :
                self.res.append(subset[::])
            return
        elif  node == self.n -1:
            self.res.append(subset[::])
            return
        
        for neighbor in self.g[node]:
            
            
            subset.append(neighbor)
            
            self.backtrack(neighbor, subset)
            
            subset.pop()
        
            
        