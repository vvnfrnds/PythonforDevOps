import sys
import subprocess

def start_server():
    print("Starting the server...")
    # Example command to start a server
    # subprocess.run(["systemctl", "start", "myservice"])
    print("Server started successfully.")

def stop_server():
    print("Stopping the server...")
    # Example command to stop a server
    # subprocess.run(["systemctl", "stop", "myservice"])
    print("Server stopped successfully.")

def restart_server():
    print("Restarting the server...")
    # Example command to restart a server
    # subprocess.run(["systemctl", "restart", "myservice"])
    print("Server restarted successfully.")

def status_server():
    print("Checking server status...")
    # Example command to check server status
    # result = subprocess.run(["systemctl", "status", "myservice"], capture_output=True, text=True)
    # print(result.stdout)
    print("Server is running.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python devops_script.py <start|stop|restart|status>")
        sys.exit(1)

    action = sys.argv[1].lower()

    if action == "start":
        start_server()
    elif action == "stop":
        stop_server()
    elif action == "restart":
        restart_server()
    elif action == "status":
        status_server()
    else:
        print("Invalid action. Use one of the following: start, stop, restart, status")
        sys.exit(1)

if __name__ == "__main__":
    main()
