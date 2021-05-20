from controller import Controller

def dbb():
    from database import Database
    database = Database()
    print(database.backup())

cntr = Controller()
