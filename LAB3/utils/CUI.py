class CUI:
  def user_auth_menu(self) -> int:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    return int(input("Enter your choice: "))

  def user_app_menu(self) -> int:
    print("1. Send message")
    print("2. Inbox messages")
    print("3. My messages statistic")
    print("4. Sign out")
    return int(input("Enter your choice: "))
  
  def admin_menu(self) -> int:
    print("1. Online users")
    print("2. Top senders")
    print("3. Top spamers")
    print("4. Exit")
    return int(input("Enter your choice: "))

  def neo_menu(self) -> int:
    print("1. (6.1) Tagged messages")
    print("2. (6.2) N long relations")
    print("3. (6.3) Shortest way")
    print("4. (6.4) Only spam conversation")
    print("5. (6.5) Tagged messages without relations")
    print("6. Exit")
    return int(input("Enter your choice: "))

  def get_tags(self) -> int:
    print("1. Add a tag")
    print("2. Exit")
    return int(input("Enter your choice: "))

  def print_list(self, name_of_list, list):
      print(name_of_list)
      count = 1
      for item in list:
          print(f"{count}: {item}")
          count += 1

  def show_way(self, nodes: list):
    way = ""
    for node in nodes:
      way += f"{node} ->"
    print(way[:-3])

cui = CUI()
