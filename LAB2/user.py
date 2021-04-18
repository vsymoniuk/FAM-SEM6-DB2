import atexit as at_exit

from utils.helpers import signed_in
from services.users import user_service
from utils.CUI import cui


def main():
    current_user_id = -1
    
    def exit_handler():
        if signed_in(current_user_id):
            user_service.sign_out(current_user_id)

    at_exit.register(exit_handler)

    while True:
        if not signed_in(current_user_id):
            choice = cui.user_auth_menu()

            if choice == 1:
                user_service.register(input("Enter your username: "))
            elif choice == 2:
                current_user_id = user_service.sign_in(input("Enter your login: "))
            elif choice == 3:
                break
            else:
                print("Wrong option selection. Enter any key to try again...")

        else:
            choice = cui.user_app_menu()

            if choice == 1:
                message = input("Enter message text: ")
                receiver = input("Enter recipient username: ")

                if user_service.create_message(message, current_user_id, recipient):
                    print("Sending message...")
            elif choice == 2:
                user_service.print_messages(current_user_id)
            elif choice == 3:
                user_service.print_messages_statistics
            elif choice == 4:
                user_service.sign_out(current_user_id)
                current_user_id = -1
            else:
                print("Wrong option selection. Enter any key to try again...")

if __name__ == "__main__":
    main()
