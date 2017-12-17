from random import randint

a = randint(1,100)

b = False

print ('猜猜我想的是什么数字？')

while b == False:

    c =  int(input())

    if c < a:
        print (str(c) + ' 太小了!')

    if c > a:
        print (str(c) + ' 太大了!')

    if c == a:
        print ('Bingo ' + str(c) + ' 正确！！！')
        b = True
