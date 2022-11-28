class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        self.winners = set()
        self.losers2count = collections.defaultdict(int)
        self.graph = collections.defaultdict(list)
        
        for w, l in matches:
            self.graph[w].append(l)
            
        for w in self.graph.keys():
            if w  not in self.losers2count:
                self.winners.add(w)
            self.dfs(w)
            
        return [sorted(list(self.winners)), sorted([loser for loser in self.losers2count if self.losers2count[loser] == 1])]
    
        
    def dfs(self, winner):
        for loser in self.graph[winner]:
            self.losers2count[loser] += 1
            if loser in self.winners:
                self.winners.remove(loser)
                

            
                
            
            
        