# import time
# d = [0] * 50
# def fibo(x):
#     if x==1 or x==2:
#         return 1
#     if d[x] !=0:
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]
#
# for num in range(5,40,10):
#     start = time.time()
#     res = fibo(num)
#     print(res,'-> 러닝 타임:', round(time.time() - start,2),'초')

d = [0]*100
d[1] = 1
d[2] = 1
N= 35
for i in range(3,N+1):
    d[i] = d[i-1] + d[i-2]

print(d[N])