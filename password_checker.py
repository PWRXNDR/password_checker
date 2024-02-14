import re

def is_strong_password(password):
    # Check the length
    if len(password) < 8 or len(password) > 23:
        return False, "Password must be 8-23 characters long."

    # Check for different character types
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit."
    if not re.search(r'\W', password):
        return False, "Password must contain at least one special character."

    # Check if password ends with a digit
    if not password[-1].isdigit():
        return False, "Password must end with a digit."

    return True, "Your password is strong!"

def password_checker():
    while True:
        password = input('Create a password (or type "exit" to quit):\n')
        if password.lower() == 'exit':
            break
        is_strong, message = is_strong_password(password)
        print(message)
        if is_strong:
            confirm_password = input('Please re-enter your password for verification: ')
            if password == confirm_password:
                print("Password verified successfully!")
                break
            else:
                print("Passwords do not match. Please try again.")
        print("\n")

# Run the password checker
password_checker()




