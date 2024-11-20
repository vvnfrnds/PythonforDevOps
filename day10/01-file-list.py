import os

folders = input("Enter the folder names separated by spaces: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
        print(f"Files in the folder '{folder}':")
        for file in files:
            print(f"  - {file}")
    except FileNotFoundError:
        print(f"Error: The folder '{folder}' does not exist. Please enter a correct folder name.")
    except PermissionError:
        print(f"Error: You do not have permission to access the folder '{folder}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
