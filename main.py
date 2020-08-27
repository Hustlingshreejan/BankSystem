




class Bank_application:

    def register_user(self):
        print("From function register")
        provide_username = input('Provide your username:')
        provide_password = input('Provide your password:')
        with open('user_info.json', 'r') as check:
            compare = check.read()
            for i in compare:
                print(i)
                if i == provide_username:
                    print("User already exits")
                else:
                    print('User created')

        # combine = f'provide_username+provide_password'
        # with open('user_info', 'w') as o:
        #     o.write(combine)






if __name__ == '__main__':
    Nepal_Bank = Bank_application()
    print("Do you have bank account?")
    try:
        user_first = int(input("Type: 1 for Yes 2 for No->"))
        if user_first == 1:
            print('Give your username and password to access your bankaccount')
            username = input("username:").capitalize()
            password = input("password:")
        elif user_first == 2:
            print("\nDo you want to make an account?")
            user_second = int(input("Type: 1 for Yes 2 for No->"))
            if user_second == 1:
                print("\nFollow the procedure to register your account")
                Nepal_Bank.register_user()

            else:
                print("Thank you for visiting our program")
                exit()
        else:
            print("Select the option carefully...")

    except Exception as e:
        print(e)
        exit()


