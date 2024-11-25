def update_server(path_to_file, key, value):
    # Read the file content
    with open(path_to_file, "r") as file:
        lines = file.readlines()

    # Write updated content
    with open(path_to_file, "w") as file:
        for line in lines:
            if line.startswith(key):  # Check for exact key match
                file.write(f"{key} = {value}\n")
            else:
                file.write(line)

# File path and parameters
path_to_file = r"D:\DevOpsLearning\11. PYTHON\Python for DevOps\day12\server.conf"
new_key = "MAX_CONNECTIONS"
new_value = "600"

# Call the function
update_server(path_to_file, new_key, new_value)
