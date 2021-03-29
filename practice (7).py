login_list = [
   'root',
   'username1'
   ]

password_list = {
   'root': '123',
   'username1': '321'
}

username = input('Введите логин:\n')

if username in login_list:
    password = input('Enter your password:\n')
    if password_list[username] == password:
        print("Welcome")
    else:
        print('Wrong password')
else:
    print('Non-existing user')
