# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

HOST = "http://www.albamon.com"
PS = 50
URL = f"{HOST}/list/gi/mon_icon_list.asp?itype=12&lvtype=1&ShortType=B&HaruDate=2019-11-14&ps={PS}"


def extract_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    total_page = soup.find(
        "div", {"class": "pageSubTit"}).em.string
    last_page = int(total_page)//PS+1
    return last_page

    # pagenation = soup.find("div", {"class": "pagenation"})

    # links = pagenation.find_all("a")
    # pages = []
    # for link in links:
    #     pages.append(link.get("data-num"))
    # print(pages)


def extract_links(last_page):
    links = []
    for page in range(last_page):
        result = requests.get(f"{URL}&page={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        cNames = soup.find_all("p", {"class": "cName"})
        for cName in cNames:
            link = cName.a.get("href")
            links.append(f"{HOST}{link}")
    return links


def extract_jobs(links):
    jobs = []
    for link in links[:2]:
        job = extract_job(link)
        jobs.append(job)
    return jobs


def extract_job(link):
    result = requests.get(link)
    # result.encoding=None
    soup = BeautifulSoup(result.text, "html.parser")
    pay_info = soup.find("div", {"class": "payInfoBox"})
    type = pay_info.find("span", {"class": "textPoint"}).get_text()
    value = pay_info.find("span", {"class": "monthPay"}).get_text()
    return {"type": type, "value": value}


def get_jobs():
    last_pages = extract_pages()
    links = extract_links(last_pages)
    jobs = extract_jobs(links)
    return jobs
