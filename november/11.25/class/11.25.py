#리스트

aaa = [1, 2, 3]

#리스트에 특정 값을 추가
aaa.append(1)
print(aaa)
#[1,2,3,1]

#리스트에서 인자값을 제거
aaa.remove(2)
print(aaa)
#2가 제거된 [1,3,1]이 출력, 1을 입력할 경우 제일 앞의 1만 제거됨.

#리스트의 맨 마지막 값을 꺼냄(전달하고 리스트에서 제거)
print(aaa.pop())
print(aaa)
#1과 [1,3]이 출력됨

#리스트의 특정 값이 몇번에 있는지 반환
print(aaa.index(1))
print(aaa)
#0과 [1,3] 출력
