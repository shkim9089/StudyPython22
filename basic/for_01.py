 # for문 학습 반복문

# arr = [1,2,3,4,5,6,7,8,9,10]

# result = 0

# for x in range(1,101):   #d인덱스와 같음 100까지하고싶으니까 101
#       result = result + x 

# print('배열의 합은 =', result)

# arr2 = ('me', 'my','friend', 'jane')

# for item in arr2:
#      print(f'{item:>10}')   #10자리로 들여써라
#      print(f'{item *2}')   #mmyymmee 



#1~10까지 수에서 짝수 구부하기

# for num in range(2,11,2):   # 마지막 2는 배수로 건너뛰기 라서 2는 짝수입니다.4는짝수입니다.
#     if (num % 2) == 0:
#         print(f'{num}는 짝수입니다.')
#     else:
#         print(f'{num}는 홀수입니다.')


# #for문 내에서 사용하는 continue,break
values = [1,3,5,7,9,11,13,15,17,19]

num = 0
for item in values:
    num += 1 # num = num+1
    if (num % 2) == 0:
        break #반복문 탈출
        #continue #of 조건만 패스 다음값으로 진행
    else:
        print(f'{num}번 수는 {item}입니다.')

