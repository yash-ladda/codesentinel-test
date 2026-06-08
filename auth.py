API_KEY = "my-secret-api-key"


def login_user(user_id):
    user = None

    if user_id > 0:
        print("User exists")

    print(user["name"])

    return True