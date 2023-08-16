import requests

import config


def get_readme(repo_detail):
    base_url = "https://api.github.com"
    headers = {"Authorization": f"token {config.TOKEN}"} if config.TOKEN else {}

    readme_url = f"{base_url}/repos/{repo_detail['repo_owner']}/{repo_detail['repo_name']}/readme"
    response = requests.get(readme_url, headers=headers)

    if response.status_code == 200:
        content = response.json()
        readme_content = content.get("content")
        if readme_content:
            import base64
            return base64.b64decode(readme_content).decode("utf-8")
        else:
            print("README not found for this repository.")
        return None
    else:
        print(f"Failed to fetch README. Status code: {response.status_code}")
        return None
