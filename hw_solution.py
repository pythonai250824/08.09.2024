# user_id: int = int(input('whats your ID:'))
# user_fname: str = input('whats your first name:')
# user_lname: str = input('whats your last name:')
# user_height: float = float(input('whats your height:'))
# user_year_birth: int = int(input('whats your year of birth:'))
#
# user_id1: int = int(input('whats your ID:'))
# user_fname1: str = input('whats your first name:')
# user_lname1: str = input('whats your last name:')
# user_height1: float = float(input('whats your height:'))
# user_year_birth1: int = int(input('whats your year of birth:'))
#
# print(
#     f"#id: {user_id:>11} name: {user_lname:<10}, {user_fname:<10} height: {user_height:.2f} year-of-birth: {user_year_birth:^6}")
# print(
#     f"#id: {user_id1:>11} name: {user_lname1:<10}, {user_fname1:<10} height: {user_height1:.2f} year-of-birth: {user_year_birth1:^6}")
#
# print(f"#id: {user_id} name: {user_lname:}, {user_fname:} height: {user_height} year-of-birth: {user_year_birth}")
# print(f"#id: {user_id1} name: {user_lname1}, {user_fname1} height: {user_height1} year-of-birth: {user_year_birth1}")
#
# grade: int = int(input('whats your grade?'))
# if 0 <= grade <= 40:
#     print("try harder next time")
# elif 41 <= grade <= 60:
#     print("you're getting there, need some more work")
# else:
#     print("illegal grade")

volume: int = int(input('whats the volume?'))
match volume:
    case 0: print('mute')
    case 1 | 2:print('very quite')
    case _:print('illegal')



