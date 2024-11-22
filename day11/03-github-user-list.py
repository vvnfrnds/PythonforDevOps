import requests

# Send GET request to the GitHub API
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON from the response
    pull_requests = response.json()

    # Loop through the list of pull requests
    for pull in pull_requests:
        # Access and print the login of the user who created the PR
        print(pull["user"]["login"])
else:
    print(f"Failed to fetch pull requests. Status code: {response.status_code}")
