import random
import string

def generate_password():
    print("Welcome to the Password Generator!")
    
    # User input for password length
    try:
        length = int(input("Enter the desired length of your password: "))
        if length < 4:  # Minimum length for a strong password
            print("Password length should be at least 4 characters.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Characters to include in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    # Display the generated password
    print(f"Your generated password is: {password}")

# Run the Password Generator
if __name__ == "__main__":
    generate_password()
