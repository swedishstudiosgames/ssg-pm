import random,string
ac=string.ascii_letters+string.digits+string.punctuation
np2=int(input("How many passwords do you need? "))
while True:
    pl=int(input("How long should each password be (between 8 and 128 characters)? "))
    if 8<=pl<=128:
        break
    print("Invalid password length. Please enter a value between 8 and 128.")
p2=set(''.join(random.choice(ac)for _ in range(pl))for _ in range(np2))
print("\n".join(p2))
with open("passwords.txt","w")as f:
    f.write("\n".join(p2))
