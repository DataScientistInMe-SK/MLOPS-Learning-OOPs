# Program to understand Class and Objects

class chatbook:
    def __init__(self):
         self.username = ""
         self.password = ""
         self.loggedin =False
         self.menu()
         
    def menu(self):
        user_input = input("""Welcome to Chatbook!! How would you like to proceed? 
                           1. Press 1 to Signup
                           2. Press 2 to Signin
                           3. Press 3 to write a post
                           4. Press 4 to message
                           5. Press any key to exit \n""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
    
    def signup(self):
        email = input(" Enter your email ID:\n")
        pwd = input(" Setup your password:\n")
        self.username = email
        self.password = pwd
        print("Signed up successfully")    
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in the main menu:\n")
        else:
            uname = input("Enter your user name or email ID:\n")
            pwd = input("Enter your password here:\n")
            if self.username == uname and self.password==pwd:
                print("You have Signed up successfully")    
                self.loggedin = True
            else:
                print("Incorrect credentials, please enter correct credentials")    
        print("\n")    
        self.menu()
       
Object1 = chatbook()