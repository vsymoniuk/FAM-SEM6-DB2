import requests
from lxml import html


def get_html_by_url(url: str):
    headers = {'Content-Type': 'text/html', }
    response = requests.get(url, headers=headers)
    return html.fromstring(response.text)
