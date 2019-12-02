# 튜플
print("tuple")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
# tuple1[1] = 10은 불가능
# 튜플은 값의 변경이나 추가, 제거가 불가능하다. 단, 2개의 튜플을 합쳐 새로운 1개를 만드는 것은 가능하다.
tuple3 = tuple1 + tuple2
print(tuple1)
print(tuple2)
print(tuple3)

print("set")
# 세트
num1 = {1, 2, 3}
num2 = {1, 4, 5}
# 세트는 집합과 같은 역할을 하는 변경 가능한 객체이다.
# 중복을 허용하지 않으며 순서가 없어 num[1]과 같은 방식으론 접근할 수 없다.
# 변경 가능하므로 값의 추가, 제거 등이 가능하다.
# 또한 집합에 대한 연산이 가능하다. ==와 같은 비교부터 union()메소드를 이용한 합집합 연산 또한 가능하다.
print(num1, num2)  # {1, 2, 3} {1, 4, 5}
print(num1 == num2)  # False
print(num1.union(num2))  # {1, 2, 3, 4, 5}
# 세트에 접근하려면 [1]이 아닌 for 문을 사용해야한다.
for i in num1:
    print(i, end=" ") # 1 2 3

print()
print("dictionary")

# 딕셔너리
# 딕셔너리는 세트와 비슷하지만 키 값과 밸류 값을 갖는 객체이다.
phoneNum = {'kim': '1234-5678', 'park': '5678-9101'}

# kim, park는 키값, 전화번호는 밸류값이 된다.
# 항목에 접근하려면 직접 접근하거나 get를 사용하면 된다.
print(phoneNum['kim'])
print(phoneNum.get('kim'))

# print(phoneNum[0]) 키값을 사용하지 않은 방식으론 접근이 불가능하다.
# 딕셔너리도 변경가능한 객체이므로 추가와 제거가 가능하다.
phoneNum['choi'] = '1111-2222'
print(phoneNum)

# 호출 후 제거는 pop, 단순 제거는 del을 사용하고 전체 제거는 clear()을 사용한다.
phoneNum.pop('kim')
del phoneNum['park']
print(phoneNum)
phoneNum.clear()
print(phoneNum)

phoneNum = {'kim': '1234-5678', 'park': '5678-9101', 'choi': '1111-2222'}
# 항목 순회는 for, 존재 여부 검사는 in, 정렬은 sorted()등을 사용한다.
# 그냥 사용하면 키값, values()를 사용하면 밸류값, items() 는 키와 값을 쌍으로 묶어 출력하는 메소드이다.
for item in phoneNum.items():
    print(item)
print('kim' in phoneNum)
print('1111-2222' in phoneNum.values())
print(sorted(phoneNum))

