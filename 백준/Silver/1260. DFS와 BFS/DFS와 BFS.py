N,M,V = map(int,input().split())

#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

#방문 리스트 행렬
visited = [0]*(N+1)

#dfs 함수 만들기
def dfs(V):
    visited[V] = 1 #방문처리
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited[i] == 0:
            dfs(i)

#bfs 함수 만들기
def bfs(V):
    queue = [V]
    visited[V] = 0 #방문처리
    while queue:
        V = queue.pop(0) #방문 노드 제거
        print(V, end = ' ')
        for i in range(1, N+1):
            if(visited[i] == 1 and graph[V][i] == 1):
                queue.append(i)
                visited[i] = 0 # 방문처리

dfs(V)
print()
bfs(V)