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

cui = CUI()
