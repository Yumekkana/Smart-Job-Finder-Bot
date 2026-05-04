import requests
from bs4 import BeautifulSoup
import html


def clean_html(raw_html):
    if not raw_html:
        return "ندارد"

    raw_html = html.unescape(raw_html)
    soup = BeautifulSoup(raw_html, "html.parser")
    text = soup.get_text(separator="\n")

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def parse_job(job):
    return {
        "title": job.get("title_farsi") or job.get("title"),
        "company": (
            job.get("employer", {}).get("name_farsi")
            or job.get("brand_data", {}).get("name_fa")
            or job.get("employer", {}).get("name")
        ),
        "location": job.get("location_text_farsi") or job.get("location_text"),
        "employment_type": job.get("employment_type", {}).get("title_farsi"),
        "salary": get_salary(job),
        "description": clean_html(
            job.get("role_description_farsi") or job.get("role_description")
        ),
        "slug": job.get("slug"),
    }


def get_salary(job):
    if not job.get("is_show_salary"):
        return "حقوق نمایش داده نشده"

    salary_from = job.get("salary_from")
    salary_to = job.get("salary_to")

    if salary_from and salary_to:
        return f"{salary_from} تا {salary_to}"
    if salary_from:
        return f"از {salary_from}"
    if salary_to:
        return f"تا {salary_to}"

    return "نامشخص"


def irantalent(keyword):
    url = "https://api.irantalent.com/api/v1/employer/position/search-by-slug"

    payload = {"keyword": keyword}

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    jobs = data.get("data", {}).get("data", [])

    cleaned_jobs = [parse_job(job) for job in jobs]

    return cleaned_jobs


# 🔥 Test
result = irantalent("پایتون")

for job in result:
    print("=" * 50)
    print(f"عنوان: {job['title']}")
    print(f"شرکت: {job['company']}")
    print(f"موقعیت: {job['location']}")
    print(f"نوع همکاری: {job['employment_type']}")
    print(f"حقوق: {job['salary']}")