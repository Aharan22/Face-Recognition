
import os

class FileManager:
    def __init__(self):
        print("Welcome to the Simple File Management System")
    
    def create_file(self, filename, content=""):
        """Create a new file with the specified filename and optional content."""
        try:
            with open(filename, 'w') as file:
                file.write(content)
            print(f"File '{filename}' created successfully.")
        except Exception as e:
            print(f"Error creating file: {e}")

    def read_file(self, filename):
        """Read the content of the file."""
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    content = file.read()
                print(f"Content of '{filename}':\n{content}")
            else:
                print(f"Error: The file '{filename}' does not exist.")
        except Exception as e:
            print(f"Error reading file: {e}")

    def write_to_file(self, filename, content):
        """Write or append content to the file."""
        try:
            with open(filename, 'a') as file:
                file.write(content)
            print(f"Content added to '{filename}' successfully.")
        except Exception as e:
            print(f"Error writing to file: {e}")

    def delete_file(self, filename):
        """Delete the specified file."""
        try:
            if os.path.exists(filename):
                os.remove(filename)
                print(f"File '{filename}' deleted successfully.")
            else:
                print(f"Error: The file '{filename}' does not exist.")
        except Exception as e:
            print(f"Error deleting file: {e}")

# Menu-driven interface for user interaction
def menu():
    fm = FileManager()

    while True:
        print("\nMenu:")
        print("1. Create a file")
        print("2. Read a file")
        print("3. Write to a file")
        print("4. Delete a file")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter the filename: ")
            content = input("Enter content (Leave empty for no content): ")
            fm.create_file(filename, content)
        elif choice == '2':
            filename = input("Enter the filename: ")
            fm.read_file(filename)
        elif choice == '3':
            filename = input("Enter the filename: ")
            content = input("Enter content to write/append: ")
            fm.write_to_file(filename, content)
        elif choice == '4':
            filename = input("Enter the filename: ")
            fm.delete_file(filename)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()

            