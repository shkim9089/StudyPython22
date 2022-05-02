# 문자역 \n 한칸 엔터, \t 탭
bruce_eckel ='Life is short,\n\tyou need Python.'
print(bruce_eckel)

multi_line = '''Life is short, 
You need python,
And i nedd c#, too.
'''
# 여러줄 문자열 '''
print(multi_line)
print(type(bruce_eckel))


#리스트(배열)

b = [1,2,3,4]

print(b)

b.append(5) #append 리스트 마지막에 추가
print(b)


# inset (자리,추가) 프로그램 랭기지는 리스트는 0부터 시작함 그래서 1(0),2(1),3(2),10(3),4(4),5(5)
b.insert(3,10)
print(b)

b.sort()  #오름차순
print(b)

b.reverse() #내림차순
print(b)

b.remove(10) # 원소 삭제
print(b)

print(type(b))


##튜플
c = (1,2,3,4)
print(c)
#c.append() # error 튜플에선 변경불가
print(c[2])


## 딕셔너리 key : values 의 집합

spiderman = {
    'name' : '피터 파커',
    'age' : 18,
    'werpon' : '웹슈터',
    'memberofavengers' : True
}
print(spiderman)
print(spiderman['name'])
print(spiderman['memberofavengers'])







