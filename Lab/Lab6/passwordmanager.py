import hashlib
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


class PasswordManager:
    def __init__(self):
        self.user_data = {}  # Hash table: username -> sha256 hash

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def register(self, username: str, password: str) -> bool:
        """Returns False if the username exists, else stores the hash and returns True."""
        if username in self.user_data:
            return False
        self.user_data[username] = self.hash_password(password)
        return True

    def login(self, username: str, password: str) -> bool:
        """True only if the user exists and the password hash matches."""
        if username not in self.user_data:
            return False
        return self.user_data[username] == self.hash_password(password)

    def register_user(self) -> None:
        username = input("Enter a username: ").strip()
        password = input("Enter a password: ")
        if self.register(username, password):
            print(f"✅ User '{username}' registered successfully.")
        else:
            print(f"❌ Username '{username}' already exists!")

    def login_user(self) -> None:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ")
        if username not in self.user_data:
            print("❌ Username not found!")
        elif self.login(username, password):
            print(f"✅ Login successful! Welcome, {username}.")
        else:
            print("❌ Incorrect password!")


def main() -> None:
    manager = PasswordManager()

    while True:
        print()
        print("1. Register User")
        print("2. Login User")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manager.register_user()
        elif choice == "2":
            manager.login_user()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()