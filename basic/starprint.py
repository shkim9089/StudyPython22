# *찍기
for x in range(1,6):
    for y in range(x,6):
        print('*', end='')
    print('')


print('hello', end=' ')  #end 델
print('world')


for x in range(1, 6):
    for y in range(x, 5):
        print(' ',end='')

    for y in range(1,x):
        print('*',end='') 

    print('')