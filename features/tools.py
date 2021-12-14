def get_user_credentials():
    with open("credentials.txt", "r") as credentials_file:
        return [x.strip('\n\r') for x in credentials_file.readlines()]
