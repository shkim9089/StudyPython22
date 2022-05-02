# if 문

from re import L


name = '홍길동'
gender = '여'

if name == '홍길동' and gender == '남':   # 흐름마지막은 콜론
        print('진료실로 들어갑니다.')
        print('의사쌤한테 인사합니다')
# 들여쓰기가 다르면 오류, 탭으로 왼쪽줄로 맞춤
else:
    print('부를때까지 기다리세요.')
    print('궁시렁거립니다')


num = 10
if num  == 9:
    print('9가 아닙니다')
else:
    print('9입니다.')