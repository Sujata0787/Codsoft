import random
import string

def generatepassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def password():
    length = int(input("Enter the desired length of the password: "))
    password = generatepassword(length)
    print("Generated Password:", password)
password()
          