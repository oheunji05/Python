#dfs
#방문한 노드는 1로 세팅하고 노드 번호 출력
#인접리스트에서 방문하지 않은 노드를 가지고 dfs 재귀 호출
def dfs(v):
    visited[v]=1 #true
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]: # i번을 방문하지 않았다면
            dfs(i)

#graph는 인접리스트로 노드를 표현한 것
graph =[ #0번은 사용 안 함
    [],           #인접행렬
    [2,3,8],      #01100001
    [1,7],        #10000010
    [1,4,5],      #10011000
    [3,5],        #00101000
    [3,4],        #00110000
    [7],          #00000010
    [2,6,8],      #01000101
    [1,7]         #10000010
]

visited=[0]*9
dfs(1) #1번 노드부터 출발 #[0,0,0,0,0...0]

# 1 2 7 6 8 3 4 5