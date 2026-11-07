class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        
        busy_servers = []
        
        answer = []
        t = 0  # 현재 가상 시간
        
        for task_idx, task_time in enumerate(tasks):
            t = max(t, task_idx)
            
            if not free_servers:
                t = max(t, busy_servers[0][0])
            
            while busy_servers and busy_servers[0][0] <= t:
                end_time, weight, idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, idx))
                
            weight, idx = heapq.heappop(free_servers)
            answer.append(idx)
            
            heapq.heappush(busy_servers, (t + task_time, weight, idx))
            
        return answer