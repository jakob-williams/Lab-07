#input username and password
userName = input("Hello! Please enter your facebook username! ")

userPassword = input("Hello! Please enter your facebook password! ")

#input validation and normalization
if(userName.lower() == "jake" and userPassword == "ProgrammingIzAight!"):
    print("Welcome to facebook!")
else:
    print("Wrong credentials, try again!")
