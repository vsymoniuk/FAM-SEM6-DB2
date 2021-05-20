import psycopg2
import os
from os import system
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time
from models.details import Details
from models.city_date import CD
from models.location import Location
import pandas as pd
import pandas.io.sql as psql
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import glob

class Database:
    def __init__(self):
        try:
            engine = create_engine('postgresql://postgres:password@localhost:5432/coursework')
            Session = sessionmaker(bind=engine)
            self.session = Session()
            print("Connected to Slave server")
            self.cursor = None
            self.connection = None
            self.connection = psycopg2.connect(user="postgres",
                                               password="password",
                                               host="localhost",
                                               port="5431",
                                               dbname="coursework")
            self.cursor = self.connection.cursor()
            print("Connected to Master server")
        except Exception as er:
            print("Error, ", er)


    def __del__(self):
        self.session.close()
        print("PostgreSQL ORM connection is closed")
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL psycopg2 connection is closed")

    def select_id(self, entity, id):
        return self.session.query(entity).get(id)

    def select_f(self, entity, any, atr):
        return self.session.query(entity).filter(atr == any).first()

    def post_details(self, add):
        post_det = Details(add)
        self.session.add(post_det)
        self.session.commit()
        return post_det

    def post_loc(self, add):
        post_loc = Location(add)
        self.session.add(post_loc)
        self.session.commit()
        return post_loc

    def post_city_date(self, add):
        post_cd = CD(add)
        self.session.add(post_cd)
        self.session.commit()

    def backup(self):
        f = open("./backups/next_backup_id.txt", "r")
        next_id = f.read()
        f.close()
        next_id = int(next_id)
        next_id_str = str(next_id + 1)
        f = open("./backups/next_backup_id.txt", "w")
        f.write(next_id_str)
        f.close()
        backup_str = f"""C:\\"Program Files"\\PostgreSQL\\11\\bin\pg_dump.exe --dbname=postgresql://postgres:password@localhost:5432/coursework > C:\\PythonProjects\\COURSEWORK\\backups\\{next_id}.dump"""
        system(backup_str)
        print(f"{next_id}.dump")
        print("Successful backup!")
        return next_id

    def restore(self):
        try:
            self.__del__()
            print("-"*65)
            os.chdir(r'C:\PythonProjects\COURSEWORK\backups')
            fl = glob.glob('*.dump')
            fl.append("close this window")
            files = pd.DataFrame(fl, columns=['filename'])
            print(files)
            backup_id = int(input('Enter file index: ').strip())
            if backup_id == 0:
                self.__init__()
                return
            os.system(rf'C:\"Program Files"\PostgreSQL\11\bin\dropdb.exe -h 127.0.0.1 -U postgres -e coursework')
            print("Drop\n", "-"*45)
            os.system(f"""C:\\"Program Files"\PostgreSQL\\11\\bin\createdb.exe -h 127.0.0.1 -U postgres -E UTF-8 -e coursework""")
            print("Create\n", "-"*45)
            if not (os.system(f"""C:\\"Program Files"\PostgreSQL\\11\\bin\psql.exe -h 127.0.0.1 -U postgres coursework < C:\\PythonProjects\\COURSEWORK\\backups\\{backup_id}.dump""")):
                print("-"*45, "\nSuccessful restore!")
                print("-"*45)
            self.__init__()
            print("-" * 45)
        except Exception as er:
            print("Error restore, ", er)

    def get_address(self):
        str = f"""select address from location"""
        df = psql.read_sql(str, self.connection)
        return df

    def func_request(self, str):
        start = time.time()
        self.cursor.execute(str)
        finish = time.time()
        tupples = self.cursor.fetchall()
        res = {
            "time": finish - start,
            "request": tupples
        }
        return res

    def f_request(self, det):
        str = f"""select d.{det["check"]}, date from details d
                            inner join city_date cd
                            on cd.id_det = d.id_det 
                                inner join location l
                                on cd.id_loc = l.id_loc and address like '%{det["address"]}%'
                                where date between '{det["start"]}' and '{det["end"]}'
                            order by d.id_det"""
        res = self.func_request(str)
        return self.plot(res, det)

    def s_request(self, det):
        str = f"""select address, avg({det["check"]}) as mini from details d
                            inner join city_date cd
                            on cd.id_det = d.id_det 
                                inner join location l
                                on cd.id_loc = l.id_loc
                                where date between '{det["start"]}' and '{det["end"]}'
                            group by address
                            order by mini"""
        res = self.func_request(str)
        return self.pie(res, det)

    def plot(self, res, det):
        listed = list(zip(*res["request"]))
        try:
            df = pd.DataFrame(np.array([speed for speed in listed[0]]), index=listed[1])
        except:
            print("No data for this period")
            exit(404)
        print(df)
        df.plot(figsize=(9, 7), title=f"Statistic in {det['address']}")
        plt.xlabel("Date")
        from view import View
        view = View().list_details()
        check = ''
        for v in view:
            if v == det["check"]:
                check = view[v]
        plt.ylabel(check)
        plt.plot(df)
        self.plt_s(df)
        print(f"Successful work for {res['time']} sec.")
        print("-"*40)
        return 1

    def plot_(self, str, det):
        start = time.time()
        df = psql.read_sql(str, self.connection)
        finish = time.time()
        time_req = finish - start
        check = det["check"]
        x = df.date
        y = df.check
        plt.figure(figsize=(9, 7))
        plt.xticks(rotation=60)
        plt.plot(x, y)
        plt.title(f"Statistic in {det['address']}")
        plt.xlabel("Date")
        from view import View
        view = View().list_details()
        checki = ''
        for v in view:
            if v == det["check"]:
                checki = view[v]
        plt.ylabel(f"Wind {checki}")
        self.plt_s(df)
        print(f"Successful work for {time_req} sec.")
        print("-"*40)
        return 1

    def pie(self, res, det):
        listed = list(zip(*res["request"]))
        try:
            df = pd.Series(np.array(listed[1]), index=listed[0], name='')
        except:
            print("No data for this period")
            exit(404)
        print(df)
        from view import View
        view = View().list_details()
        check = ''
        for v in view:
            if v == det["check"]:
                check = view[v]
        explode = []
        for i in range(1, df.size):
            explode.append(0)
        explode.append(0.2)
        df.plot.pie(figsize=(9, 7), explode=explode, title=f"Statistic for {check}", shadow=True,
                    autopct='%1.1f%%', startangle=45)
        self.plt_s(df)

    def vis(self):
        try:
            f = open("./visualizations/next_plt_id.txt", "r")
            next_id = f.read()
            f.close()
            next_id = int(next_id)
            next_id_str = str(next_id + 1)
            f = open("./visualizations/next_plt_id.txt", "w")
            f.write(next_id_str)
            f.close()
            print(next_id)
            return next_id
        except Exception as er:
            print("Error,", er)

    def plt_s(self, df):
        id = self.vis()
        plt.savefig(f"./visualizations/{id}.png")
        plt.plot(df)

    def buff_indx(self):
        names = ['First', 'Second', 'Third']
        # conditions
        values1 = [0.079536, 0.121840, 0.089604]
        values2 = [0.000862, 0.038000, 0.008260]
        # address
        values3 = [0.001452, 0.000308, 0.000209]
        values4 = [0.000042, 0.000035, 0.000015]

        plt.figure(figsize=(16, 7))

        plt.subplot(131)
        plt.bar(names, values4)
        plt.subplot(132)
        plt.scatter(names, values4)
        plt.subplot(133)
        plt.plot(names, values4)
        plt.suptitle('Request')

    def request_a1(self, det):
        str = f"""select d.{det["check"]}, date from details d
                                    inner join city_date cd
                                    on cd.id_det = d.id_det 
                                        inner join location l
                                        on cd.id_loc = l.id_loc and address like '%{det["address"]}%'
                                        where date between '{det["start"]}' and '{det["end"]}'
                                    order by d.id_det"""
        str1 = f"""select d.{det["check"]}, date from details d
                                    inner join city_date cd
                                    on cd.id_det = d.id_det 
                                        inner join location l
                                        on cd.id_loc = l.id_loc and address like '%{det["address1"]}%'
                                        where date between '{det["start"]}' and '{det["end"]}'
                                    order by d.id_det"""
        print(str, str1)
        res = self.func_request(str)
        res1 = self.func_request(str1)
        return self.analysis(res, res1, det)

    def analysis(self, res, res1, det):
        try:
            df = pd.DataFrame(res["request"])
            df1 = pd.DataFrame(res1["request"])
        except:
            print("No data for this period")
            exit(404)
        df[1] = pd.to_datetime(df[1], format='%Y%m%d %H:%M:%S').dt.floor('d')
        df = df.groupby(df[1]).mean()
        df1[1] = pd.to_datetime(df1[1], format='%Y%m%d %H:%M:%S').dt.floor('d')
        df1 = df1.groupby(df1[1]).mean()
        sec = (df1.index).tolist()
        labels = [ts.strftime("%Y-%m-%d") for ts in sec]
        country = (df[0]).tolist()
        country1 = (df1[0]).tolist()

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, country, width, label=det["address"])
        rects2 = ax.bar(x + width / 2, country1, width, label=det["address1"])

        from view import View
        view = View().list_details()
        check = ''
        for v in view:
            if v == det["check"]:
                check = view[v]
        ax.set_ylabel(check)
        ax.set_title(f'{check} in {det["address"]} and {det["address1"]}')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        fig.tight_layout()
        plt.xticks(rotation=90)
        id = self.vis()
        plt.savefig(f"./visualizations/{id}.png")

    def request_a2(self, det):
        str = f"""select address, avg({det["check"]}) as mini from details d
                            inner join city_date cd
                            on cd.id_det = d.id_det 
                                inner join location l
                                on cd.id_loc = l.id_loc
                                where date between '2020-12-01' and '2021-01-01'
                            group by address
                            order by mini
                            LIMIT 10"""
        res = self.func_request(str)
        return self.pie(res, det)