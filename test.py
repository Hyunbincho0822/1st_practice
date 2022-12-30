import random

rsp = ['s', 'r', 'p']
result = {0: '승리!', 1: '패배!', 2: '무승부!'}
money = int(input("가지고 있는 돈을 알려주세요"))
bet = int(input('배팅 금액을 입력해주세요'))

com_random = random.randint(0, 2)
com = rsp[com_random]

while True:
    user = input("가위 바위 보")
    if not user in rsp:
        print("다시 입력해주세요")
    else:
        break

print('-----------------------------------')
print(f'사용자 : {user}')
print(f'컴퓨터 : {com}')

state = 0
if user == com:
    state = 2
elif user == 's' and com == 'r':
    state = 1
    money = money - bet
elif user == 'r' and com == 'p':
    state = 1
    money = money - bet
elif user == 'p' and com == 's':
    state = 1
    money = money - bet
else:
    state = 0
    money = money + bet

print(result[state])
print("-----------------------------------")

print("남은 돈")
print(money)