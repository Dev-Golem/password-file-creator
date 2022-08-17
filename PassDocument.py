def main():
    file1 = open('C:/Users/'+os.getlogin()+"/Desktop/password.txt", "a")
    name = input("What's the name of the site?: ")
    name = str(name)
    user = input("What's the username?: ")
    name_user = input("What is the name associated with the account?: ")
    password = input("What's the password?: ")
    email = str(input("What's the email for the account?(0 for nothing): "))
    if len(email) == 0:
        email = "N/A"
    if len(name) == 0:
        name = "N/A"
    if len(name_user) == 0:
        name_user = "N/A"
    if len(password) == 0:
        password = "N/A"
    if len(user) == 0:
        user = "N/A"
    file1.write("\n\n")
    file1.write(name)
    file1.write("\nEmail - ")
    file1.write(email)
    file1.write(":\n")
    file1.write("User - ")
    file1.write(user)
    file1.write("\nPass - ")
    file1.write(password)
    file1.close()
    print("Completed")
main()