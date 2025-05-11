import hashlib

# Hashing function to secure plain text passwords
def hash_password(user_password):
    return hashlib.sha256(user_password.encode()).hexdigest()

# Verifies login credentials by comparing stored and entered password hashes
def verify_login(user_email, entered_password, saved_credentials):
    if user_email in saved_credentials:
        hashed_stored_password = saved_credentials[user_email]
        return hashed_stored_password == hash_password(entered_password)
    return False

# Main function to run the login system
def main():
    # Simulated database of email-password (hashed) pairs
    saved_credentials = {
        "user@example.com": hash_password("password123"),
        "hani@gmail.com": hash_password("mypassword"),
    }

    print("\n🔐 Welcome to Secure Login System\n")
    user_email = input("📧 Email: ")
    entered_password = input("🔑 Password: ")

    if verify_login(user_email, entered_password, saved_credentials):
        print("\n✅ Access granted! Welcome back.")
    else:
        print("\n❌ Access denied! Email or password is incorrect.")

if __name__ == '__main__':
    main()
