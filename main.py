import csv




class Bank_application:
    ''' This function checks whether the username is already present in dataset or not. If its new, will add if not, ask for new username '''
    def register_user(self):
        username = input('Provide your username:').capitalize()
        with open(r'C:\Users\dell\Desktop\Dataforprojects\saveddata.csv', 'r') as checking_username:
            dataset = csv.reader(checking_username)
            header = next(dataset)
            for data in dataset:
                if username == data[0]:
                    print("\nUsername already exits. Try another username.".upper())
                    Nepal_Bank.register_user()
            else:
                print(f"Your username \"{username}\" has been approved by the bank")
                password = input('Provide your password:')
                with open(r'C:\Users\dell\Desktop\Dataforprojects\saveddata.csv', 'a', newline='') as saving_newuser:
                    writer = csv.writer(saving_newuser)
                    # writer.writerow(["Username", "Password"])
                    writer.writerow([username, password])
                print("\nCongratulation!!!\nYour bank account has been created. Now you can deposit and withdraw the money")


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


