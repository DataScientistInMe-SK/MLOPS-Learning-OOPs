# Program to understand Class and Objects

class chatbook:
    
# Define hidden varibale for generating incremental Customer ID
    __user_id = 0

    def __init__(self):
         self.id = chatbook.__user_id
         chatbook.__user_id += 1
         self.__name = "John Doe jr."
         self.username  = ""
         self.password = ""
         self.loggedin =False
        #  self.menu()
    
    
    @staticmethod
    def get_id():
        return chatbook.__user_id

    @staticmethod
    def set_id(value):
        chatbook.__user_id   = value
    
    # Getter and Setter
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name= value
         
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
            self.mypost()
        elif user_input == "4":
            self.sendmessage()
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
    
    def mypost(self):
        if self.loggedin == True:
            message = input("Enster your post or message here:\n")
            print(f"Following message has been posted {message}")
        else:
            print("Please signin first to write the post")    
        print("\n")    
        self.menu()
        
    def sendmessage(self):
        if self.loggedin == True:
            message = input("Enter your post or message here:\n")
            Friend_user = input("Whom would you like to send the message:\n")
            print(f"Your message has been sent to {Friend_user}")
        else:
            print("Please signin first to write the post")    
        print("\n")    
        self.menu()
                
             
User1 = chatbook()
print(User1.username)