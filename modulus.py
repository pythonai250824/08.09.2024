
#  9         1 --> modulus %
# ___ =   4 ___
#  2         2

#  8         2 --> modulus %
# ___ =   2 ___
#  3         3

#  8         0 --> modulus %
# ___ =   4 ___
#  2         2

#   12        4 --> modulus
#  ____ =  1 ___
#    8        8

# modulus == 0 ?

# 5/2 = 2.5

number: int = int(input('enter a number'))

if number % 2 == 0:
    print('zugi') # even
else:
    print('e-zugi') # odd

print(9//2)

# input number
# check if number can be divided by 7
# if yes print 7-Boom else print not-7-boom

if number % 7 == 0:
    print('7 Boom')
else:
    print('Not 7 Boom')

# input number
# 49
# asarot -- 4 tens digit
# ahadot -- 9 ones digit

# 70
# asarot -- 7
# ahadot -- 0

# input 2-digit number 78
# print the asarot 7
# print the ahadot (?) 8

asarot: int = number // 10
print(number // 10)
ahadot: int = number % 10
print(number % 10)

print(f"asarot {asarot} ahadot {ahadot}")

#  78          8 --> modulus
# ____  =  7 ____
#  10         10

#  90          0 --> modulus
# ____  =  9 ____
#  10         10

# go for trip
# each car 5 moshavim
# x
# how many cars of 5?
# how many people in the last?

# x input
# 14
# 2 cars of 5 = total 10
# 1 cars of 5 with 4

# 26
# 5 cars of 5 = total 25
# 1 cars of 5 with 1

# 45
# 9 cars of 5 = total 45
# 0 cars more ...

# modulus == 0 ?

# 50 / 5 = 10
# 50 % 5 = 0

# 52 // 5 = 10
# 52 % 5 = 2
#   52          2
#  ____  = 10  ___
#    5          5

passengers = int(input('how many travellers?'))
cars = passengers // 5
print(f'cars = {passengers // 5}')
# if passengers % 5 != 0:
# if not passengers % 5 == 0:
if passengers % 5 != 0:
    print(f'another car for {passengers % 5}')




