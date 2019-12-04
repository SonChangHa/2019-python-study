# 재귀함수를 통한 피보나치수열 계산기

def myfib(a):
    if a == 0: return 0
    if a == 1: return 1
    return myfib(a - 1) + myfib(a - 2)


for i in range(15):
    print(myfib(i), end=' ')

# 재귀함수는 자기가 자기를 호출하기 때문에 값이 커지면 시간이 오래걸린다.
# myfib(100)을 하면 0까지 거슬러 올라가며 호출해야하기 때문.
