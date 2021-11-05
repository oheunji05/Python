# 물 구덩이 수 구하기

# 4 5
# 00110
# 00011
# 11111
# 00000
# 출력
# 3

# 첫 번째 줄에 땅 크기 N,M   1<=N, M<=1000
# 두 번째 줄에 N+1번째 줄까지 땅에 대한 표시이다.
# 0은 물 구덩이, 1은 밟아도 무너지지 않는 땅이다.
# 전체 땅 속에서 물 구덩이 개수를 출력한다

n,m=map(int,input().split()) #split은 띄어쓰기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m: # 땅의 경계선
        return False

    if graph[x][y]==0: #0이 있으면
        graph[x][y]=1 #1로 바꿀 것이다
        dfs(x-1,y) #
        dfs(x,y-1) #
        dfs(x+1,y) #
        dfs(x,y+1) #
        return True
    return False

cnt=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            cnt+=1
print(cnt)