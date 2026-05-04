import requests
from urllib.parse import urlencode

allowed_sorts = ["relevance_desc", "published_at_desc", "salary_from_desc"]
allowed_locations = ["", "تهران", "خراسان رضوی", "البرز", "اصفهان", "مازندران", "قم", "فارس", "خوزستان"
                     , "گیلان", "کرمان", "آذربایجان شرقی", "یزد", "هرمزگان", "گلستان", "اردبیل", "قزوین",
                     "بوشهر", "کرمانشاه", "مرکزی", "همدان", "سیستان و بلوچستان","آذربایجان غربی",
                     "چهارمحال بختیاری", "سمنان", "زنجان", "کردستان", "خراسان شمالی", "ایلام", "خراسان جنوبی"
                     , "لرستان", "کهکیلویه و بویراحمد"]

def jobinja(categories, keyword, locations, sort_by):

    params = {
        "filters[job_categories][]": categories,
        "filters[keywords][0]": keyword,
        "filters[locations][]": locations,
        "sort_by": sort_by,
    }

    url = "https://jobinja.ir/jobs?" + urlencode(params)

    headers = {
    'referer': 'https://jobinja.ir/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    }

    response = requests.request("GET", url, headers=headers)

    return response.text
