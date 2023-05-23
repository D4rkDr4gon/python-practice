import heapq
import sys

# algoritmo de Dijkstra

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0

    while heap:
        d, u = heapq.heappop(heap)

        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

n, m, start = map(int, input().split())

adj = [[] for _ in range(n + 1)]
dist = [sys.maxsize] * (n + 1)

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

dijkstra(start)

for i in range(1, n + 1):
    if dist[i] == sys.maxsize:
        print("INF")
    else:
        print(dist[i])
