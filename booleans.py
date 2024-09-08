
x: int = 5
f: float = 9.7
name: str = "danny"

yes: bool = True
no: bool = False

is_vegan: bool = True

if is_vegan == True:
    print('offer beyond burger')
else:
    print('offer beef burger')

balance: int = 10_000_000
is_rich: bool = balance > 1_000_000

# longer
if balance > 1_000_000:
    is_rich = True
else:
    is_rich = False

is_rich: bool = balance > 1_000_000  # shorter

if is_vegan:
    print('offer beyond burger')
else:
    print('offer beef burger')

if is_rich and not is_vegan:
    print('offer filet mignon')

if is_rich == True and is_vegan == False:
    print('offer filet mignon')

# input age
# if the age is bigger equal 18 then is_old_enough = True otherwise be False
# if old enough offer Beer otherwise offer juice

age = int(input('Whats your age?'))
is_adult: bool = age >= 18

if is_adult:
    print('Offer Beer')
else:
    print('offer Juice')

# if True  and True  == True
# if True  and False == False
# if False and True  == False [short]
# if False and False == False [short]

# if True  or True  == True   [short]
# if True  or False == True   [short]
# if False or True  == True
# if False or False == False

number: int = 90
is_zero: bool = number == 0
is_number_not_zero = number != 0

is_adult: bool = age >= 18
# is_adult True  -- 1
# is_adult False -- 0

number = int(input('input number'))
# if number != 0:
# if number is not zero and number is bigger than 20
#if number and number > 20:
#if number != 0 and number > 20

# name: str = input('whats your name?')
# if name: # if name has some value











