import heapq
import bisect




class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        answer = []
        free_server = [i for i in range(k)]
        heapq.heapify(free_server)
        busy_server = []

        status = {i : 0 for i in range(k)}

        t = 0
        live = k
        for i, arrive in enumerate(arrival):
            t = max(t, arrive)

            # 반납
            while busy_server and busy_server[0][0] <= t:
                _, server = heapq.heappop(busy_server)
                heapq.heappush(free_server, i + (server - i) % k)

            # 사용 가능한 서버 없을 시 드랍
            if not free_server:
                continue

            # print(free_server)
            peak_server = heapq.heappop(free_server)
            cur_server = peak_server % k

            heapq.heappush(busy_server, (t + load[i], cur_server))
            status[cur_server] += 1
        

            

        # print(status)

        max_l = max(status.values())
        for k, v in status.items():
            if v == max_l:
                answer.append(k)

        return answer