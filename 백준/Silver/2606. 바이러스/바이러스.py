from collections import deque
from sys import stdin


def bfs(V):
    count = 0
    queue = deque([V])
    visited[V] = 1  # 처음 시작을 방문처리
    while queue:
        V = queue.popleft()  # 방문 노드 제거
        # print(V, end=" ")
        count += 1
        for i in range(1, com + 1):
            if visited[i] == 0 and graph[V][i] == 1:
                queue.append(i)
                visited[i] = 1  # 방문처리
    return count - 1


input = stdin.readline
com = int(input())
node = int(input())

# 방문 리스트 행렬
visited = [0] * (com + 1)

# 이차원 배열로 그래프 그리기
graph = [[0] * (com + 1) for _ in range(com + 1)]
for i in range(node):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


# 방문 기록 작성하기 : 1번에서 파생된 노드만 지나는 방문기록
print(bfs(1))