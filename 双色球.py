from random import randint

import random

a=range(1,34)

print ('红球是：')
print (random.sample(a,6))

blue_ball_1 = randint(1,16)

print ('蓝球是：')
print ('[' + str(blue_ball_1) + ']')
