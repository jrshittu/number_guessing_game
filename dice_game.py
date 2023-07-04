from random import randint

ai_choice = randint(1, 6)

def get_input():
    global user_input
    user_input = input('Kindly choose between Odd and Even')
    try:
        if user_input in ('Even', 'Odd'):
            return user_input
    except ValueError:
        pass
    print('Try again 🧡')
    user_input = input('Kindly choose between Odd and Even')
    
get_input()
if ai_choice % 2 == 0 and user_input == 'Even':
    print('You rock😍🙌👏')
    
elif ai_choice % 2 == 1 and user_input == 'Odd':
    print('You rock😍🙌👏')
else: 
    print('Haha🤣😛')