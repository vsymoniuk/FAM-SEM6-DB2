from utils.CUI import cui
from services._neo4j import neo4j

def main():
    while True:
        choice = cui.neo_menu()

        if choice == 1:
            tags = input("Enter a tags, separated by a comma: ")
            users_with_tagged_messages = neo4j.get_users_with_tagged_messages(tags)
            cui.print_list("Users: ", users_with_tagged_messages)

        elif choice == 2:
            n = int(input("Enter the 'N' value: "))
            users_with_n_long_relations = neo4j.get_users_with_n_long_relations(n)
            cui.print_list("Users: ", users_with_n_long_relations)

        elif choice == 3:
            username1 = input("Enter username of the first user")
            username2 = input("Enter username of the second user")
            way = neo4j.shortest_way_between_users(username1, username2)
            cui.show_way(way)

        elif choice == 4:
            users_which_have_only_spam_conversation = neo4j.get_users_which_have_only_spam_conversation()
            cui.print_list("Users: ", users_which_have_only_spam_conversation)

        elif choice == 5:
            tags = input("Enter a tags, separated by a comma: ")
            unrelated_users_with_tagged_messages = neo4j.get_unrelated_users_with_tagged_messages(tags)
            cui.print_list("Users: ", unrelated_users_with_tagged_messages)

        elif choice == 6:
            break

        else:
            print("Wrong option selection. Enter any key to try again..")


if __name__ == '__main__':
    main()