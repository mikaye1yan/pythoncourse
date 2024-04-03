class User:
    user_count = 0  
    def __init__(self, username):
        self.username = username
        User.user_count += 1  
u1 = User("johnsmith10")
print(User.user_count)  
print(u1.username)      
u2 = User("marysue1989")
print(User.user_count)  
print(u2.username)     
u3 = User("milan_rodrick")
print(User.user_count) 
print(u3.username)     