# 파일 입출력 2 - 파일 읽기

f = open(file='./temp.txt',mode='r',encoding='utf-8')

# t = f.read() #전체
while True:
    line = f.readline()  #한줄씩 읽기
    if not line: break

    print(line, end='')    


# print(t)

f.close() #필수

print('파일 읽기 완료')


