import requests
import json

def jobvision(keyword):
  url = "https://candidateapi.jobvision.ir/api/v1/JobPost/List"

  payload = json.dumps({
    "pageSize": 30,
    "requestedPage": 1,
    "keyword": keyword,
    "sortBy": 1,
    "searchId": None
  })
  headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'ngsw-bypass': 'true',
    'origin': 'https://jobvision.ir',
    'priority': 'u=1, i',
    'referer': 'https://jobvision.ir/',
    'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    'web-app-version': '19.0.120'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  result = response.json()
  jobposts = result['data']['jobPosts']
  joblist = []
  for jobpost in jobposts:
    data =  {
    'job title': jobpost['title'],
    'link': f"https://jobvision.ir/jobs/{jobpost['id']}"
  }
    joblist.append(data)
  return joblist
