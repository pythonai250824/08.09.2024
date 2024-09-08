
number: int = 1
is_number_empty: bool = number == 0

name: str = input('whats your name?')
if name: # if name has some value
    print('something inside')
else:
    print('empty')

is_name_empty: bool = not name

if not name: # if name has some value
    print('empty')
else:
    print('something inside')

# if name and check_first_charachter

# Question 2
# if 4 < 9: ? True
