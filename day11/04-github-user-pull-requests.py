import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

if response.status_code == 200:

    pull_requests = response.json()

    pr_counts = {}
    for pull in pull_requests:
        user = pull["user"]["login"]        #Extract the username
        if user in pr_counts:
            pr_counts[user] = pr_counts[user] + 1
        else:
            pr_counts[user] = 1

    #Print number of pull requests by each user
    for user, count in pr_counts.items():
        print(f"{user}:{count} pull requests")

else:
    print("There are no pull requests")
