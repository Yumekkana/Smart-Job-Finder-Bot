import requests
import json

def irantalent(keyword):

    url = "https://api.irantalent.com/api/v1/employer/position/search-by-slug"

    payload = json.dumps({
    "keyword": keyword
    })
    headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.irantalent.com',
    'Referer': 'https://www.irantalent.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text
