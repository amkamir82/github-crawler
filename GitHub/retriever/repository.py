import config
import requests


def get_name(repo_detail):
    return [repo_detail["repo_name"]]


def get_file_names(repo_detail):
    base_url = f"https://api.github.com/repos/{repo_detail['repo_owner']}/{repo_detail['repo_name']}/git/trees/master?recursive=5"
    headers = {
        "Authorization": f"token {config.TOKEN}",
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        tree_data = response.json()
        file_names = [entry['path'] for entry in tree_data['tree'] if entry['type'] == 'blob']
        return file_names
    else:
        print(f"Failed to fetch data from GitHub API. Status code: {response.status_code}")
        return []


def get_description(repo_detail):
    base_url = f"https://api.github.com/repos/{repo_detail['repo_owner']}/{repo_detail['repo_name']}"
    headers = {
        "Authorization": f"token {config.TOKEN}",
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        repo_data = response.json()
        description = repo_data['description']
        return [description]
    else:
        print(f"Failed to fetch repository data from GitHub API. Status code: {response.status_code}")
        return None


def get_topics(repo_detail):
    base_url = f"https://api.github.com/repos/{repo_detail['repo_owner']}/{repo_detail['repo_name']}"
    headers = {
        "Authorization": f"token {config.TOKEN}",
        'Accept': 'application/vnd.github.mercy-preview+json'
    }

    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        repo_data = response.json()
        topics = repo_data['topics']
        return topics
    else:
        print(f"Failed to fetch repository data from GitHub API. Status code: {response.status_code}")
        return []


def get_labels(repo_detail):
    base_url = f"https://api.github.com/repos/{repo_detail['repo_owner']}/{repo_detail['repo_name']}/labels"
    headers = {
        "Authorization": f"token {config.TOKEN}",
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        labels_data = response.json()
        labels = [label['name'] for label in labels_data]
        return labels
    else:
        print(f"Failed to fetch repository labels from GitHub API. Status code: {response.status_code}")
        return []


def get_contributors(repo_detail):
    base_url = f"https://api.github.com/repos/{repo_detail['repo_owner']}/{repo_detail['repo_name']}/contributors"
    headers = {
        "Authorization": f"token {config.TOKEN}",
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        contributors_data = response.json()
        contributor_logins = [contributor['login'] for contributor in contributors_data]
        return contributor_logins
    else:
        print(f"Failed to fetch contributors from GitHub API. Status code: {response.status_code}")
        return []

