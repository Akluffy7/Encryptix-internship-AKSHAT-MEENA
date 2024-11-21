#password generator
import random
import string

def generate_password(length):
 
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    
    all_characters = lowercase + uppercase + digits + symbols


    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length < 1:
                print("Enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")


    generated_password = generate_password(length)


    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()
