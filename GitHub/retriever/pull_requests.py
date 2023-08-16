import requests
import config


def get_all_pull_requests(repo_detail):
    base_url = f"https://api.github.com/repos/{repo_detail['repo_owner']}/{repo_detail['repo_name']}/pulls"
    headers = {
        "Authorization": f"token {config.TOKEN}",
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        pull_requests_data = response.json()
        return pull_requests_data
    else:
        print(f"Failed to fetch pull requests from GitHub API. Status code: {response.status_code}")
        return []


def get_changed_files_in_pr(repo_detail):
    prs = get_all_pull_requests(repo_detail)
    for pr in prs:
        base_url = f"{pr['url']}/files"
        headers = {
            "Authorization": f"token {config.TOKEN}",
            'Accept': 'application/vnd.github.v3+json'
        }

        response = requests.get(base_url, headers=headers)

        if response.status_code == 200:
            pr_files_data = response.json()
            changed_files = [file['filename'] for file in pr_files_data]
            return changed_files
        else:
            print(
                f"Failed to fetch pull request #{pr} files from GitHub API. Status code: {response.status_code}")
            return []


def get_review_comments(repo_detail):
    prs = get_all_pull_requests(repo_detail)
    result = []
    for pr in prs:
        headers = {
            "Authorization": f"token {config.TOKEN}",
            'Accept': 'application/vnd.github.v3+json'
        }

        response = requests.get(f'{pr["url"]}/comments', headers=headers)

        jason_response = response.json()
        reviews = [(i['path'], [j for j in i['diff_hunk'].split('\n')[1::]],
                    i['body']) for i in jason_response]
        for i in reviews:
            before = []
            after = []
            for j in i[1]:
                if str(j).startswith("-"):
                    before.append(j[1::])
                elif str(j).startswith("+"):
                    after.append(j[1::])
                else:
                    after.append(j)
                    before.append(j)

            result.append({"url": pr["url"], "before": before, "after": after, "comment": i[2]})

    return result
