
# START

x: int = 0
if x or True:
    print()

while x <= 11:
    print(x)
    x = x + 1 # x += 1

print('finish')

x = 2
while x < 20:
    # if x % 2 == 0:
    #     print(x)
    print(x)
    x = x + 2 # x += 1

x = int(input('enter number:'))
while x < 20:
    if x % 2 == 0:
        print(x)
    x = x + 1

# 7 --> 8 10 12 14 16 18 20
# 8 --> 8 10 12 14 16 18 20
if not x % 2 == 0:
    x = x + 1
while x <= 20:
    print(x)
    x = x + 2

x = int(input(x))
while x >= 0: # x != 0
    print(x)
    x = x - 1

# STOP