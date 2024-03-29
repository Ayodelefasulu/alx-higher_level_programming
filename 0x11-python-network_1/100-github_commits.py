#!/usr/bin/python3
"""
This script takes in a repository name and owner name as arguments, and uses
the GitHub API to list 10 commits (from the most recent to oldest) of the
specified repository by the specified owner.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:  # Get the 10 most recent commits
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error fetching commits:", response.status_code)
