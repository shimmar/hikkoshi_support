import requests
from bs4 import BeautifulSoup
import time
import re

class RoomInfo():
    def __init__(self):
        self.name="" #物件名
        self.rent=-1 #家賃
        self.management=-1 #管理費・共益費
        self.shikikin=-1 #敷金
        self.reikin=-1 #礼金
        self.floor=-1 #階数
        self.madori="" #間取り
        self.area=-1 #面積
        self.old=-1 #築年数
        self.nearest_station="" #最寄り駅
        self.station_distance=-1 #駅徒歩
        self.made_of="" #材質
    
    def get_monthly_rent(self):
        return self.rent+self.management

def search_number(target, match_flag=False):
    pattern="[0-9\.]+"
    if not match_flag:
        result=re.search(pattern, target)
    else:
        result=re.match(pattern, target)
    if result:
        return result.group()
    else:
        return 0

def get_room_info(url):
    room_info=RoomInfo()
    article=requests.get(url)
    soup= BeautifulSoup(article.text, 'html.parser')

    #物件名の取得
    room_info.name=soup.select_one(".section_h1-header-title").text

    rent_info=soup.select(".property_view_note-list")

    #家賃、管理費・共益費の取得
    rent_list1=rent_info[0].contents
    rent=search_number(rent_list1[1].text,True)
    management=search_number(rent_list1[3].text)
    room_info.rent=int(float(rent)*10000)
    room_info.management=int(management)

    #敷金、礼金の取得
    rent_list2=rent_info[1].contents
    shikikin=search_number(rent_list2[1].text)
    reikin=search_number(rent_list2[3].text)
    room_info.shikikin=int(float(shikikin)*10000)
    room_info.reikin=int(float(reikin)*10000)

    #階数、間取り、面積、築年数、最寄り駅、駅徒歩の取得
    details=soup.select_one(".property_view_table").contents
    for data in details:
        header=data.th.text
        print(header)

    print(room_info.name)
    print(room_info.rent)
    print(room_info.management)
    print(room_info.shikikin)
    print(room_info.reikin)

get_room_info(input())