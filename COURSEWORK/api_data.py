import requests
from view import View
view = View()

url = "https://visual-crossing-weather.p.rapidapi.com/history"


headers = {
    "x-rapidapi-key": "c0b6079824mshb67731cbbd5a826p1d6f32jsnd81a06f9d181",
    "x-rapidapi-host": "visual-crossing-weather.p.rapidapi.com"
}

def get_():
    defaults = view.choose_d()
    response = []
    for default in defaults:
        querystring = {
            "startDateTime":f"{default['start_date']}",
            "aggregateHours":f"{default['times']}",
            "location":f"{default['location']}",
            "endDateTime":f"{default['end_date']}",
            "unitGroup":"us",
            "dayStartTime":"8:00:00",
            "contentType":"csv",
            "dayEndTime":"17:00:00",
            "shortColumnNames":"0"
            }

        res = requests.request("GET", url, headers=headers, params=querystring)
        response.append(res)
        view.line()
        print(res.text)
        view.line()
    return response