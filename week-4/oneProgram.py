username = input("Username: ")
password = input("Password: ")

if (username != "brendhatasca"):
    print("Access denied. Credentials not found.")
elif (password != "python123"):
    print("Wrong password.")
else: 
    print("Access granted.")