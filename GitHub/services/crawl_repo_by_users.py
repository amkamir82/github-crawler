import requests
import config


def retrieve_all_users():
    users = []
    id = 0
    last_user_id = 0
    while id <= config.LAST_USER_ID:
        response = requests.get(f"https://api.github.com/users?since={id}")
        jason_response = response.json()
        print(jason_response)
        for user_data in jason_response:
            try:
                users.append((user_data["login"], last_user_id := user_data["id"]))
            except Exception as e:
                print(user_data)
        id = last_user_id
        print(id)


retrieve_all_users()
