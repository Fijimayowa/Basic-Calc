user_input=int(input('Please enter your first number: '))
user_second_input=int(input('Please enter yout second number: '))
command=input('Type in command to begin program: ')

try:
    if command=='divide':
        var=user_input/user_second_input
        print(f'{user_input}/{user_second_input}={var}')
except ZeroDivisionError:
    print('Error!! Divided by 0')
try:
    if command=='multiply':
        var2=user_input*user_second_input
        print(f'{user_input}*{user_second_input}={var2}')
    elif command=='add':
        var3=user_input+user_second_input
        print(f'{user_input}+{user_second_input}={var3}')
    elif command=='subtract':
        var4=user_input-user_second_input
        print(f'{user_input}-{user_input}={var4}')
except ValueError:
    print('Error key value error')