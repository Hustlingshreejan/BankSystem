import csv

class Bank_application:
    def user_auth(self):
        print('\nGive your username and password to access your bankaccount')
        username = input("username:").capitalize()
        with open(r'C:\Users\dell\Desktop\Dataforprojects\saveddata.csv', 'r') as auth:
            auth_data = csv.reader(auth)
            header = next(auth_data)
            remaining_data = [a for a in auth_data]
            for data in remaining_data:
                if username == data[0]:
                    password = input("password:")
                    if password == data[1]:
                        print('Username and password correct.')
                        print(f'Currently, you have {data[2]} in your bank account')
                        user_forth = int(input('1: deposit 2: withdraw 3: Exit'))
                        if user_forth == 1:
                            in_int = int(data[2])
                            deposite_amt = int(input('Enter the amount you want to deposit:'))
                            updated_amt = in_int + deposite_amt
                            print(f'Now you have {updated_amt} in your bank account.')
                            data[2] = str(updated_amt)
                            with open(r'C:\Users\dell\Desktop\Dataforprojects\saveddata.csv', 'w', newline='') as w:
                                writer = csv.writer(w)
                                writer.writerow(['Username', 'Password', 'Balance'])
                                writer.writerows(remaining_data)
                        elif user_forth == 2:
                            in_int = int(data[2])
                            withdraw_amt = int(input('Enter the amount you want to deposit:'))
                            updated_amt = in_int - withdraw_amt
                            print(f'The remaining amount in your account is {updated_amt}')
                            data[2] = str(updated_amt)
                            with open(r'C:\Users\dell\Desktop\Dataforprojects\saveddata.csv', 'w', newline='') as w:
                                writer = csv.writer(w)
                                writer.writerow(['Username', 'Password', 'Balance'])
                                writer.writerows(remaining_data)
                        else:
                            exit()
                    else:
                        print('Username or password wrong. Try again...')
                        Nepal_Bank.user_auth()
                    break
            else:
                print('Invalid user. If you do not have an account, please create one.')
                user_third = int(input("1: sign-up, 2: sign-in"))
                if user_third == 1:
                    Nepal_Bank.register_user()
                else:
                    Nepal_Bank.user_auth()

    def register_user(self):
        ''' This function checks whether the username is already present in dataset or not. If its new, will add if not, ask for new username '''
        username = input('Provide your username:').capitalize()
        with open(r'C:\Users\dell\Desktop\Dataforprojects\saveddata.csv', 'r') as checking_username:
            dataset = csv.reader(checking_username)
            header = next(dataset)
            for data in dataset:
                if username == data[0]:
                    print("\nUsername already exits. Try another username.".upper())
                    Nepal_Bank.register_user()
                    break
            else:
                print(f"Your username \"{username}\" has been approved by the bank.")
                password = input('Provide your password:')
                with open(r'C:\Users\dell\Desktop\Dataforprojects\saveddata.csv', 'a', newline='') as saving_newuser:
                    writer = csv.writer(saving_newuser)
                    writer.writerow([username, password, 0])
                    print("\nCongratulation!!!\nYour bank account has been created. Now you can check the balance, deposit and withdraw the money\n"
                          "You are now directed to login section.")
                    saving_newuser.close()
                    Nepal_Bank.user_auth()


if __name__ == '__main__':
    Nepal_Bank = Bank_application()
    print("Do you have bank account?")
    try:
        user_first = int(input("Type: 1 for Yes 2 for No->"))
        if user_first == 1:
            Nepal_Bank.user_auth()
        elif user_first == 2:
            print("\nDo you want to make an account?")
            user_second = int(input("Type: 1 for Yes 2 for No->"))
            if user_second == 1:
                print("\nFollow the procedure to register your account.")
                Nepal_Bank.register_user()
            else:
                print("Thank you for visiting our bank's system.")
                exit()
        else:
            print("Select the option carefully...")
    except Exception as e:
        print(e)
        exit()


