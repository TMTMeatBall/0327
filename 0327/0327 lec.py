# 팩토리얼 재귀함수 호출
# n을 대입한 단계를 먼저, 재귀호출이므로 n-1,n-2,n-3....return 1이 되는 순간까지 계속함
# def fact(n):
#     if n <=1:
#         return 1
#     else:
#         return n*fact(n-1)

# 반복/재귀의 차이 정리

# 완전 탐색과 baby-gin
# 순열, 조합 (백트래킹과도 연관?)
# 0번 인덱스에 숫자를 정해 두고 1번 인덱스를 정하고....i>n이 된 순간 출력하도록 설정

# perm(i,k)
#     if i==k:
#         print array // 원하는 작업 수행
#     else:
#         for j:i -> k-1
#             p[i] <-> p[j]
#             perm(n+1,k)
#             p[i]<->p[j]

def perm(i, k):
    if i == k:
        print(*p)
    else:
        for j in range(i, k):  # 자기 자신부터 오른쪽 원소들과 자리를 교환
            p[i], p[j] = p[j], p[i]
            perm(i + 1, k)
            p[i], p[j] = p[j], p[i]


p = [1, 2, 3]
perm(0, 3)

# 자리는 바꾸는 것과 사전적 순서
# 자리를 바꾸지 않는 다른 계산방식 사용하지 않은  숫자를 if used[j] == 0: used
def perm(i,k):
    if i == k:
        print(*p)
    else:
        for j in range(k): #사용하지 않은 숫자를
            if used[j]==0: #used에서 순서대로 검색
                p[i]=A[j]
                used[j] = 1 #j번자리 숫자 사용했음을 표시
                perm(i+1,k)
                used[j] = 0 #j번 자리 숫자를 다른 자리에서 쓸 수 있게

A = [1,2,3]
p = [0] * 3
used = [0] * 3
perm(0,3)

#기본적으로 순열이 생성되는 방법을 이해
