def update_server(path_to_file,key,value):
    with open(path_to_file,"r") as file:
        lines = file.readlines()

    with open(path_to_file,"w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

server_config_path = r"D:\DevOpsLearning\11. PYTHON\Python for DevOps\day12\server.conf"
new_key = "MAX_CONNECTIONS"
new_value = "12300"

update_server(server_config_path, new_key, new_value)