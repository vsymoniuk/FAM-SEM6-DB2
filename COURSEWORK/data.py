from io import StringIO
import json
import csv
from datetime import datetime

class Data:
    def __init__(self):
        self.csvFilePath = r'data_files/data.csv'
        self.jsonFilePath = r'data_files/data.json'

    def make_json(self):
        from api_data import get_ as raw
        response = raw()
        d = 1
        ch = True
        for res in response:
            data = {}
            if res.text != '{"message":"You have exceeded the MONTHLY quota for Requests on your current plan, BASIC. Upgrade your plan at https:\/\/rapidapi.com\/visual-crossing-corporation-visual-crossing-corporation-default\/api\/visual-crossing-weather"}':
                csvReader = csv.DictReader(res.iter_lines(decode_unicode=True))
            else:
                if ch:
                    print("Error, RES SERVER IS NULL")
                    ch = False
                continue
            for rows in csvReader:
                key = rows['Date time']
                data[key] = rows
            with open(f'data_files/{d}.json', 'w', encoding='utf-8') as jsonf:
                jsonf.write(json.dumps(data, indent=4))
            d = d + 1
        return d-1

    def obj_4_analyse(self):
        try:
            res = []
        except Exception as er:
            print(er, 404)

    def obj_4_post(self, d):
        try:
            res = []
            with open(f'data_files/{d}.json') as jsonf:
                data = json.load(jsonf)
                for obj in data:
                    times = data[obj]['Date time']
                    data[obj]['Date time'] = datetime.strptime(times, '%m/%d/%Y %H:%M:%S')
                    res.append(data[obj])
            return res
        except Exception as er:
            print(er, 404)