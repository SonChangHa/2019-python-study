import random

list = []



while True:
    a = int(input("please enter the num. if you wants stop, enter 0>> "))
    if a == 0:
        break
    list.append(a)


print("sort algorithm. 1:bogo,")
b = int(input("enter the algorithm"))

if b == 1:
    #bogosort

    while True:
        if i+1 < len(list):
            if list[i] > list[i+1]:
                random.shuffle(list)
                i = 0
            else:
                print(list)
                break
