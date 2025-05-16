# Program to understand Class and Objects

class chatbook:
    def __init__(self):
         self.username = ""
         self.password = ""
         self.loggedin =False
         self.menu()
         
    def menu(self):
        user_input = input("""Welcome to Chatbook!! How would you like proceed? 
                           1. Press 1 to Signup
                           2. Press 2 to Signin
                           3. Press 3 to write a post
                           4. Press 4 to message
                           5. Press any key to exit \n""")
        if user_input == '1':
            pass
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()
        
       
Object1 = chatbook()