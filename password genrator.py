import string
import random

def generate_password(length, use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length should be positive number.")
            return
        
        special_input = input("Include special characters?(y/n): ").strip().lower()
        if special_input =='y':
            use_special_chars =True
        elif special_input =='n':
            use_special_chars =False
        else:
            print("Invalid input.")
            use_special_chars = True
        
        password = generate_password(length, use_special_chars)
        print("Your Generated password:", password)

    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    main()
