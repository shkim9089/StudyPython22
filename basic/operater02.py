# 문자열 연산
from platform import python_branch
from tkinter import CURRENT


first = 'Hello'
second = 'Wordl'

print(first + second) # 문자열연산 + 합치기
print(first, second) # CONCAST문자열 띄움


print(first * 3) #문자열연산 *,+ 만 있음

#문자열 길이 내장함수
print(len('한글'))
print(len(first))

#리스트 연산
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])
#print(first[-6]) # index 엘러 큰문제


## 현재 일시
current_date = '2022-05-02 14:23:45'
year = current_date[0:4]
month = current_date[5:7]
day = current_date[8:10]
hour = current_date[11:13]
min = current_date[14:16]
sec = current_date[17:19]


print(year,'년', month,'월',day,'일')
print(hour,'시', min,'분', sec, '초')

print(current_date[-5:-3])

#문자열은 리스트 
p = 'python'
print(p)
#p[0] = 'P' #python
p2='P'+ p[1:]
print(p2)

print(p.upper())
print(p2.lower())
