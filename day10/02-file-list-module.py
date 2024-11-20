import os

def list_of_files(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder Not Found"
    except PermissionError:
        return None, "No Permissions"

def main():
    folders = input("enter the folder names separate by space: ").split()

    for folder in folders:
        files, error_message = list_of_files(folder)
        if files:
            print(f"Files in {folder}")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder} : {error_message}")

if __name__ == "__main__":
    main()