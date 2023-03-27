dx = [0, 1]
dy = [1, 0]


def dfs(x, y, sum):
    global answer
    if answer <= sum:
        return  # pruning
    if x == N - 1 and y == N - 1:  # 도착지 arr[N-1][N-1]
        if answer > sum:
            answer = sum
        return  # 종료 조건

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx and nx < N and ny > -1 and ny < N:
            dfs(nx, ny, sum+arr[nx][ny])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 10000
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {answer}')
