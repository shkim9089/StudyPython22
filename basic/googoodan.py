# 구구단 프로그램  
# 2x1 = 2 ... 2x0 = 18
# 3x1 = 3 ....3x9 = 27 x x y = xy
# 9x1 = 9 ... 9x9 = 81

print('---구구단 프로그램---')

for x in range(2, 10):                  # 2부터 9까지인데 +1로 맞춰서 10
    print(f'{x}단 시작')                #첫 단의 프린트
    for y in range(1, 10):              # 1뷰토 9까지인데 +1이라서 10
        print(f'{x}x{y}={x*y:2d}',end=' ') # : 숫자+d(정수)로 표현하겠다   end는 엔터를 ' '로 바꾼거임
    print() #단마다 줄 맞추기위한 집어넣음