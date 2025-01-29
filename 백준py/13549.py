"""
13549. 숨바꼭질3

list를 -1로 초기화한다.
시작자리는 0
시작을 q에 넣고 -1, +1, 2배를 확인 후
- 더 작으면 update and q에 넣기
- 아니면 next
다 돌았을 때 list 출력

-> 시간복잡도가 문제일 듯
O(3N) "1초에 2천만번!!"

실수한 부분
1. N이랑 K 범위를 마음대로 생각해서
graph를 K까지만 만들었다.
K+1에서 -1로 오는 경우도 있기 때문에 100001로 만들어야함

2. next의 범위체크에서 
0<=next<K로 했는데 이러면 K+1에서 -1로 오는 경우 체크를 못한다.

결론
graph는 N, K에 종속되게 만드는 것보다
그냥 최댓값에 대해 만드는 게 마음 편하다
"""

from collections import deque

N, K = map(int, input().split())
graph = [-1]*(100001)

graph[N] = 0
q = deque([N])

while q:
    now = q.popleft()
    
    # 2배
    next = 2*now
    if 0 <= next <= len(graph) - 1 and (graph[next] == -1 or graph[next] > (graph[now])):
        graph[next] = graph[now]
        q.append(next)

    # +-1초
    for d in (1,-1):
        next = now + d
        if 0 <= next <= len(graph) - 1 and (graph[next] == -1 or graph[next] > (graph[now]+1)):
            graph[next] = graph[now]+1
            q.append(next)


#print(graph)
print(graph[K])