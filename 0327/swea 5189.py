def dfs(n, sum, current): #방문한 구역 수 n, 합계 sum, 현재 위치 current
    global answer #
    if answer <= sum: #answer<=sum인 경우? non-promising 이므로 더 하지 않고 다른 경로 탐색한다.
        return

    if n == N: #dfs탐색이 종료되는 시점.
        answer = min(answer, sum + arr[current][1])
        return

    for i in range(2, N + 1): #1은
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1, sum + arr[current][i], i)
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    #0이 들어가는 int 를 사용한 이차원 배열의 선언

    answer = 10000
    visited = [0] * (N + 1)

    dfs(1, 0, 1) #(방문한 구역 수가 1이고, sum=0 ,현위치 1에서 dfs를 시행한 값)
    print(f'#{tc} {answer}')

# 사무실에서 출발해서 (1번) / 관리구역을 돌고 / 다시 사무실로 온다 (1번)
# 각 구역을 한 번씩만 방문하고, 사무실로 돌아올 때만을 생각한다.
# 그 때의 배터리 사용이 최소가 되는 경우의 사용량은?
