from database import Database
from datetime import datetime
from models.location import Location
from data import Data
from view import View

class Controller:
    def __init__(self):
        self.enter = {}
        self.now = datetime.now()

        self.csvFilePath = r'data.csv'
        self.jsonFilePath = r'data.json'
        self.database = Database()
        self.data = Data()
        self.view = View()
        self.table = None
        self.hello()

    def hello(self):
        try:
            self.view.hello()
            while True:
                res = self.view.main_()
                if res == "1":
                    self.get_data()
                elif res == "2":
                    self.graphs_plot()
                elif res == "3":
                    self.graphs_pie()
                elif res == "4":
                    self.database.backup()
                elif res == "5":
                    self.database.restore()
                elif res == "6":
                    self.analysis()
                elif res == "7":
                    self.top()
                elif res == "8":
                    self.view.bye()
                    break
                else:
                    self.view.inc()
        except Exception as er:
            print("Error,", er)

    def get_data(self):
        res = self.data.make_json()
        self.db_post_data(res)

    def graphs_plot(self):
        res = self.database.get_address()
        ans = self.view.graph_plot(res)
        self.database.f_request(ans)

    def analysis(self):
        res = self.database.get_address()
        ans = self.view.analysis(res)
        self.database.request_a1(ans)

    def top(self):
        ans = self.view.top()
        self.database.request_a2(ans)

    def graphs_pie(self):
        ans = self.view.graph_pie()
        self.database.s_request(ans)

    def db_post_data(self, d):
        try:
            for i in range(1, d+1):
                res = self.data.obj_4_post(i)
                for post in res:
                    d = self.db_post_det(post)
                    hm = self.database.select_f(Location, post["Address"], Location.address)
                    if hm is None:
                        l = self.db_post_loc(post)
                        id_l = l.id_loc
                    else:
                        id_l = hm.id_loc
                    post["id_loc"] = id_l
                    post["id_det"] = d.id_det
                    self.db_post_cd(post)
        except Exception as er:
            print(er, 404)

    def db_post_det(self, add):
        return self.database.post_details(add)

    def db_post_cd(self, add):
        self.database.post_city_date(add)

    def db_post_loc(self, add):
        return self.database.post_loc(add)