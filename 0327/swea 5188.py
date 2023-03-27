dx = [0, 1]  # 아래 이동
dy = [1, 0]  # 오른쪽 이동


def dfs(x, y):
    global tmp, result #글로벌 지정해야 함
    if result < tmp:
        return

    if x == N - 1 and y == N - 1:
        result = tmp
        return

    for i in range(2):  # 우하 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if (nx, ny) not in visited:
            visited.append((nx, ny))
            tmp += arr[nx][ny]
            dfs(nx, ny)
            tmp -= arr[nx][ny]
            visited.remove((nx, ny))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    tmp = arr[0][0]  # 현재 어디에 위치하는지 (시작점 [0][0]
    visited = []  # 방문지점은 여기에 append한다
    result = 11111
    dfs(0, 0)  # [0][0]을 출발점으로 하는 dfs를 시행.
    print(f'#{tc} {result}')



# NxN판에서 00위치에서 22위치로 감.
# 오른쪽,왼쪽으로만 이동 가능
# 숫자합계는 최소가 되어야 함
# dfs를 쓰면, visited에 담고, 앞으로 방문할 곳에 담고
# queue.append(start_node)
# stack = list()
# while stack:
#     node = stack.pop()
#     if node not in visited:
#         visited.append(node)
#         stack.extend(graph[node])
