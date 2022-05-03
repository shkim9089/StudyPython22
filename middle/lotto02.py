# 번호에다가 가중치를 준 프로그램

import random as rnd

numbers = weights = [i for i in range(1,46)]
lotto = []   #로또번호 저장
rnd.shuffle(weights)

lotto = rnd.choices(numbers,weights=weights, k=6)
lotto.sort()
print(lotto)