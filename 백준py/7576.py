"""
7576. 토마토

입력
M N (가로, 세로)
1은 익은, 0은 익지않음, -1은 토마토 x
토마토가 모두 익는 최소날짜
만일 불가하다면 -1 출력

로직
- 입력
- 토마토 모두 집어넣기 (큐에)
- 익은 토마토에 대해서 현재날짜+1하면서 bfs
- 큐가 비면 모든 토마토 익었는지 체크하고 출력

BFS
- Queue 필요
- FIFO
- Visited

공부할 것
1. BFS 동작방법
2. 시간복잡도 계산해보기

<2. 시간복잡도>
NM = 10^6
"""

M, N = map(int, input().split()) # M:가로, N:세로
graph = [list(map(int, input().split())) for _ in range(N)]

from collections import deque
q = deque([])
for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            q.append((y,x))
#visited = [[False]*M for _ in range(N)]


# 익은 토마토에 대해서 bfs
while q:
    y, x = q.popleft()
    for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
        ny = y + dy
        nx = x + dx
        if 0<=ny<N and 0<=nx<M and graph[ny][nx] == 0:
            graph[ny][nx] = graph[y][x] + 1
            q.append((ny,nx))
                # visited[ny][nx] = 


# 만약 0이 있으면 -> -1
for line in graph:
    if 0 in line:
        print(-1)
        exit()

# 그 외에는 day - 1
M = 0
for line in graph:
    M = max(M, max(line))
print(M-1)
