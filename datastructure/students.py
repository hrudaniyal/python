students = {
    "hruda": 85,
    "alok": 78,
    "deepak": 92,
    "david": 88,
    "utkal": 95
}
while True:
    user_input = input('enter your name : ')
    if user_input in students :
        print(f"{user_input}'s mark is : {students[user_input]}")
        break ;
    else :
        print('user not found !!!')
        print('try again________')
        
