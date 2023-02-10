import hashlib,os,getpass,sqlite3
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def password_manager():
    os.makedirs("accounts",exist_ok=True)
    os.chdir("accounts")
    conn=sqlite3.connect("passwords.db")
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS passwords (username text,password text)")
    while True:
        print("1.Create account\n2.Login\n3.Quit")
        choice=input("Enter your choice: ")
        if choice=="1":
            print("Create new account")
            username=input("Username: ")
            password=getpass.getpass("Password: ")
            hashed_password=hash_password(password)
            c.execute("INSERT INTO passwords VALUES (?,?)",(username,hashed_password))
            conn.commit()
            print("Account created!")
        elif choice=="2":
            print("Login")
            username=input("Username: ")
            password=getpass.getpass("Password: ")
            c.execute("SELECT password FROM passwords WHERE username=?",(username,))
            result=c.fetchone()
            if result:
                if hash_password(password)==result[0]:
                    print("Login successful!")
                else:
                    print("Incorrect password")
            else:
                print("Account does not exist")
        elif choice=="3":break
        else:
            print("Invalid choice")
    conn.close()
if __name__=="__main__":
    password_manager()
