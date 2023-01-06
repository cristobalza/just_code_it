class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        manhattan = lambda pt1, pt2 : abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])
        
        idx_2_dist_idx_tuple = collections.defaultdict(list)
        
        for i in range(n):
            for j in range(i + 1, n):
                pt1 = points[i]
                pt2 = points[j]
                
                distance = manhattan(pt1, pt2)
                
                idx_2_dist_idx_tuple[i].append([distance, j])
                idx_2_dist_idx_tuple[j].append([distance, i])
            
        # Prism
        res = 0
        minheap = [[0,0]] # [distance, idx]
        visited = set()
        
        while len(visited) < n :
            dist, idx = heapq.heappop(minheap)
            if idx in visited: continue
            visited.add(idx)
            res += dist
            for neighbor_dist, neighbor_idx in idx_2_dist_idx_tuple[idx]:
                if neighbor_idx not in visited:
                    heapq.heappush(minheap, [neighbor_dist, neighbor_idx])
                    
        return res