import requests

# ANSI color codes for styling
BOLD = "\033[1m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Send a GET request to fetch the list of pull requests from the GitHub API
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# Check if the API call was successful (HTTP status code 200 indicates success)
if response.status_code == 200:

    # Parse the response JSON into a Python list
    pull_request = response.json()

    # Dictionary to store the number of pull requests created by each user
    pr_counts = {}

    # Loop through each pull request in the list
    for pull in pull_request:
        user = pull["user"]["login"]        # Loop through each pull request in the list
        if user in pr_counts:               # If the user is already in the dictionary, increment their count
            pr_counts[user] += 1
        else:
            pr_counts[user] = 1

    
    print(f"\n{BOLD}{BLUE}The list of Pull Requests are: {RESET}")
    for user, count in pr_counts.items():
        print(f"{user}:{count} pull requests")

    # .strip() removes any leading or trailing whitespace from the input for accurate matching
    key_to_delete = input("enter the user you wish to delete: ").strip()     
    if key_to_delete in pr_counts:
        del pr_counts[key_to_delete] 
        print(f"\n{BOLD}Deleted the user {key_to_delete}{RESET}")
    else:
        print(f"\n{BOLD}User couldnt be found {key_to_delete}{RESET}")

    print(f"\n{BOLD}{BLUE}Updated list of users are{RESET}")
    for user, count in pr_counts.items():
        print(f"{user}:{count} Pull Requests")

else: 
    print(f"\n{BOLD}Failed to fetch Pull Requests: {response.status_code}{RESET}")