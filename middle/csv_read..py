#<!-- csv파일 읽기 -->

import csv

file_name ='busanbus_211231.csv'

f = open(file_name,mode='r',encoding='cp949')
reader = csv.reader(f,delimiter=',') #구분자가 ',' 인경우

next(reader) ## 제목줄이 있을때 첫번째 제목줄 삭제

for line in reader:                          # 쉬프트 딜리트
    print(line)


f.close()  ##필수
