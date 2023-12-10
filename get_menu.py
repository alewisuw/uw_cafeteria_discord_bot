from bs4 import BeautifulSoup
import requests
import re

def get_menu(date):
    r = requests.get("https://uwaterloo.ca/food-services/locations-and-hours/daily-menu?field_uw_fs_dm_date_value%5Bvalue%5D%5Bdate%5D=" + date)
    soup = BeautifulSoup(r.content, "lxml")
    all_links = soup.find_all('a') 

    cmh = []
    v1 = []

    checkpoint = False
    count = 0
    for link in all_links:
        link_text = str(link.get_text())
        if "Daily menu for " in link_text:
            checkpoint = True
        if checkpoint == True:
            if count < 1:
                count+=1
                next
            elif count <= 6:
                cmh.append(re.sub(' +', ' ', link_text))
                count+=1
            elif count > 6:
                res = re.search(r'"(.*?)"', str(link))
                res = (res.group(1))
                v1.append(f"[{re.sub(' +', ' ', link_text)}](<https://uwaterloo.ca/{res}>)")
                if link_text[:5] == "Build":
                    break
                count+=1
    print(v1)
    return [cmh, v1]

get_menu("2022-02-11")