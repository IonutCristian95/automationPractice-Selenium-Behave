import os

def get_user_credentials():
    with open(os.getcwd()+os.sep+"features"+os.sep+"credentials.txt", "r") as credentials_file:
        return [x.strip('\n\r') for x in credentials_file.readlines()]
