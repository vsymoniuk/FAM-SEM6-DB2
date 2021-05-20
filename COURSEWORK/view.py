from datetime import date, datetime, timedelta
import calendar
import dateutil.parser as dpar

class View:
    def __init__(self):
        self.enter = {}
        self.ch = True
        self.now = datetime.now()
        default = {"start_date": "2002-08-03", "end_date": "2002-08-10", "times": "6", "location": "Berezan,UA"}

    def input_date(self):
        try:
            B = False
            P = True
            res = 'er'
            dates = {}
            year = mouth = 0
            while True:
                try:
                    dates["year"] = input("Enter a year: ")
                    if dates["year"] == "":
                        P = False
                        return res;
                    else:
                        year = int(dates["year"])
                        if year < int(self.now.strftime("%Y")):
                            B = True
                        if year > int(self.now.strftime("%Y")):
                            print("Input the year more than now. Try again. ")
                            continue
                        break
                except:
                    print("Input error. Try again. ")
                    continue

            while True:
                try:
                    if (not P):
                        break
                    dates["mouth"] = input("Enter a mouth: ")
                    if dates["mouth"] == "":
                        print("You don't enter mouth. Try again.")
                        continue
                    mouth = int(dates["mouth"])
                    if (not B) and mouth > int(self.now.strftime("%m")):
                        print("Input the mouth more than now. Try again. ")
                        continue
                    elif (not (mouth > 0 and mouth < 13)):
                        print("Input the mouth incorrect. Try again.")
                        continue
                    break
                except:
                    print("Input error. Try again. ")
                    continue

            res = f'{year}-{mouth}-1'
            return res
        except Exception as er:
            print("Error in input_date", er)

    def api_data(self):
        try:
            default_ = {"start_date": "2002-08-03", "end_date": "2002-08-10", "times": "6", "location": "Berezan,UA"}
            while True:
                self.line()
                choose = input("Enter the first letter of the country you want: ").lower()
                if choose == "":
                    return default_
                f = open(f"./cntry_cptl/{choose}.txt", "r")
                cn_cap = f.read()
                f.close()
                print(cn_cap)
                self.line()
                self.enter["location"] = input("Enter the suggested location: ")
                self.line()
                if self.enter["location"] == "":
                    self.enter["location"] = default_["location"]
                break
            while True:
                try:
                    self.enter["times"] = int(input("Enter a times: "))
                    self.line()
                    if self.enter["times"] is None:
                        self.enter["times"] = default_["times"]
                    break
                except:
                    print("Input error. Try again. ")
                    continue
            while True:
                print("Enter a start date: \n")
                re1 = self.input_date() #self.enter["start_date"]
                self.line()
                print("Enter a end date: \n")
                re2 = self.input_date() #self.enter["end_date"]
                res1 = dpar.parse(re1)
                res2 = dpar.parse(re2)
                if res1 > res2:
                    continue
                else:
                    break
            poi = int(((res2 - res1).days * ((12 / self.enter["times"]) + 1))/90)
            start_dates = []
            res = []
            start_dates.append(str(res1.date()))
            check = res1.date()
            for i in range(1, poi+1):
                if self.ch:
                    date = check
                    days_in_month = calendar.monthrange(date.year, date.month)[1]
                    date += timedelta(days=days_in_month)
                    check = date
                    start_dates.append(str(date))
                    self.ch = False
                else:
                    date = check + timedelta(days=1)
                    start_dates.append(str(date))
                    days_in_month = calendar.monthrange(date.year, date.month)[1]
                    date += timedelta(days=days_in_month-1)
                    check = date
                    start_dates.append(str(date))
            for i in range(0, poi*2-1):
                if i % 2 == 0:
                    ress = {"start_date": start_dates[i], "end_date": start_dates[i+1],
                           "times": self.enter["times"], "location": self.enter["location"]}
                    res.append(ress)
            return res
        except Exception as er:
            print("Error in api_data", er)

    def choose_d(self):
        while True:
            try:
                choose = int(input("Choose how to generate data?\n1. Defaults.\n2. Input filter.\n>> "))
                self.line()
                if choose == 1:
                    default_ = [{"start_date": "2019-01-01T00:00:00", "end_date": "2019-01-07T00:00:00", "times": 6, "location": "Washington,DC,USA"}]
                    return default_
                elif choose == 2:
                    return self.api_data()
                else:
                    print("Entered number is incorrect. Try again.")
                    continue
            except:
                print("Input error. Try again. ")
                continue

    def inc(self):
        print("Wrong command. Try again.")
        self.line()

    def hello(self):
        self.line()
        print("WELCOME! THIS IS COURSEWORK! THIS PROGRAM IS ABOUT THE WEATHER.")
        self.line()

    def main_(self):
        print("Choose what you want to do:")
        res = input("1. Get data.\n2. Graphs(line) of details.\n3. Graphs(pie) of details.\n4. Backup.\n"
                    "5. Restore.\n6. Analysis countries.\n7. Top 10.\n8. Exit.\n>> ")
        self.line()
        return res

    def bye(self):
        print("Goodbye!")
        self.line()

    def line(self):
        print("-"*40)

    def list_details(self):
        det = {"min_tem": "Minimum Temperature",
               "max_tem": "Maximum Temperature",
               "wind_speed": "Wind Speed",
               "wind_dir": "Wind Direction",
               "dew_point": "Dew Point",
               "precipitation": "Precipitation",
               "visibility": "Visibility",
               "could_cov": "Cloud Cover",
               "relative_hum": "Relative Humidity"}
        return det

    def pr_list(self, det):
        for key, value in det.items():
            print(key, '->', value)

    def graph_plot(self, res):
        try:
            ans = {}
            default = {"address": "Monaco,Monaco",
                       "check": "wind_speed",
                       "start": "2015-01-01",
                       "end": "2015-04-01"}
            print(res)
            ans["address"] = input("\nEnter address: ")
            if ans["address"] == "":
                ans["address"] = default["address"]
            self.pr_list(self.list_details())
            ans["check"] = input("\nChoose what you want to analyze: ")
            if ans["check"] == "":
                ans["check"] = default["check"]
            while True:
                self.line()
                print("Enter interval.")
                print("Enter a start date: \n")
                ans["start"] = re1 = self.input_date()  # self.enter["start_date"]
                if ans["start"] == 'er':
                    ans["start"] = re1 = default["start"]
                self.line()
                print("Enter a end date: \n")
                ans["end"] = re2 = self.input_date()  # self.enter["end_date"]
                # print(ans["end"] == 'er')
                if ans["end"] == 'er':
                    ans["end"] = re2 = default["end"]
                self.line()
                res1 = dpar.parse(re1)
                res2 = dpar.parse(re2)
                if res1 > res2:

                    continue
                else:
                    break
            return ans
        except Exception as er:
            print("Error, ", er)

    def graph_pie(self):
        try:
            ans = {}
            default = {"check": "wind_speed",
                       "start": "2015-01-01",
                       "end": "2015-04-01"}
            self.line()
            self.pr_list(self.list_details())
            ans["check"] = input("\nChoose what you want to analyze: ")
            if ans["check"] == "":
                ans["check"] = default["check"]
            while True:
                self.line()
                print("Enter interval.")
                print("Enter a start date: \n")
                ans["start"] = re1 = self.input_date()  # self.enter["start_date"]
                if ans["start"] == 'er':
                    ans["start"] = re1 = default["start"]
                self.line()
                print("Enter a end date: \n")
                ans["end"] = re2 = self.input_date()  # self.enter["end_date"]
                if ans["end"] == 'er':
                    ans["end"] = re2 = default["end"]
                self.line()
                res1 = dpar.parse(re1)
                res2 = dpar.parse(re2)
                if res1 > res2:
                    continue
                else:
                    break
            return ans
        except Exception as er:
            print("Error, ", er)

    def analysis(self, res):
        try:
            ans = {}
            default = {"check": "wind_speed",
                       "address": "Monaco,Monaco",
                       "address1": "Belarus,Minsk",
                       "start": "2015-01-01",
                       "end": "2015-02-01"}
            print(res)
            ans["address"] = input("\nEnter first address: ")
            if ans["address"] == "":
                ans["address"] = default["address"]
            self.line()
            ans["address1"] = input("Enter second address: ")
            if ans["address1"] == "":
                ans["address1"] = default["address1"]
            self.line()
            self.pr_list(self.list_details())
            ans["check"] = input("\nChoose what you want to analyze: ")
            if ans["check"] == "":
                ans["check"] = default["check"]
            while True:
                self.line()
                print("Enter interval.")
                print("Enter a start date: \n")
                ans["start"] = re1 = self.input_date()  # self.enter["start_date"]
                if ans["start"] == 'er':
                    ans["start"] = re1 = default["start"]
                self.line()
                print("Enter a end date: \n")
                ans["end"] = re2 = self.input_date()  # self.enter["end_date"]
                if ans["end"] == 'er':
                    ans["end"] = re2 = default["end"]
                self.line()
                res1 = dpar.parse(re1)
                res2 = dpar.parse(re2)
                if res1 > res2:

                    continue
                else:
                    break
            return ans
        except Exception as er:
            print("Error, ", er)

    def top(self):
        try:
            ans = {}
            default = {"check": "wind_speed"}
            self.pr_list(self.list_details())
            ans["check"] = input("\nChoose what you want to analyze: ")
            if ans["check"] == "":
                ans["check"] = default["check"]
            return ans
        except Exception as er:
            print("Error, ", er)