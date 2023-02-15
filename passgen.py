import random,string
ascii_chars=string.ascii_letters+string.digits+string.punctuation
num_passwords=int(input("How many passwords do you need? "))
while True:
    password_length=int(input("How long should each password be (between 8 and 128 characters)? "))
    if 8<=password_length<=128:
        break
    print("Invalid password length. Please enter a value between 8 and 128.")
passwords=set(''.join(random.choice(ascii_chars)for _ in range(password_length))for _ in range(num_passwords))
print("\n".join(passwords))
with open("passwords.txt","w")as f:
    f.write("\n".join(passwords))