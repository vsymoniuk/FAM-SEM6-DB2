from threading import Thread

from db.connection import connection
from utils.CUI import cui


def main():
    while True:
        print()
        choice = cui.admin_menu()

        if choice == 1:
            online_users = connection.smembers("online:")
            print("Users online:")
            for index, user in enumerate(online_users):
                print(f"{index + 1}. {user}")

        elif choice == 2:
            senders = connection.zrange("sent:", 0, 4, desc=True, withscores=True)
            print("Top 5 senders:")
            for index, sender in enumerate(senders):
                username = sender[0].replace("user:", "")
                messages_count = sender[1]
                print(f"{index + 1}. {username} - {messages_count} message(s)")

        elif choice == 3:
            spamers = connection.zrange("spam:", 0, 4, desc=True, withscores=True)
            print("Top 5 spamers:")
            for index, spamer in enumerate(spamers):
                username = spamer[0].replace("user:", "")
                messages_count = spamer[1]
                print(f"{index + 1}. {username} - {messages_count} spammed message(s)")

        elif choice == 4:
            break
        else:
            print("Wrong option selection. Enter any key to try again..")


if __name__ == '__main__':
    main()
