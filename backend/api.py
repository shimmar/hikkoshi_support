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
        self.direction="" #向き
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

    #階数、間取り、面積、築年数、向き、最寄り駅、駅徒歩の取得
    details=soup.select(".property_view_table-title")
    for detail in details:
        header=detail.text
        if header=="階":
            room_info.floor=int(search_number(detail.next_sibling.next_sibling.text, True))
        elif header=="間取り":
            room_info.madori=detail.next_sibling.next_sibling.text
        elif header=="専有面積":
            room_info.area=float(search_number(detail.next_sibling.next_sibling.text, True))
        elif header=="築年数":
            room_info.old=int(search_number(detail.next_sibling.next_sibling.text))
        elif header=="向き":
            direction=detail.next_sibling.next_sibling.text
            if direction!="-":
                room_info.direction=direction
        elif header=="駅徒歩":
            stations=detail.next_sibling.next_sibling
            #最寄り駅と徒歩分数を決定する

    #材質の取得
    material_label=soup.select_one(".data_table").tr.select_one(".data_02")
    if material_label.text=="構造":
        material=material_label.next_sibling.next_sibling.text
        if "木造" in material:
            room_info.made_of="木造"
        elif "軽量鉄骨" in material:
            room_info.made_of="軽量鉄骨"
        elif "鉄筋コン" in material:
            room_info.made_of="鉄筋コン"
        elif "気泡コン" in material:
            room_info.made_of="気泡コン"
        elif "鉄骨鉄筋" in material:
            room_info.made_of="鉄骨鉄筋"
        elif "鉄骨" in material:
            room_info.made_of="鉄骨"

    print(room_info.name)
    print(room_info.rent)
    print(room_info.management)
    print(room_info.shikikin)
    print(room_info.reikin)
    print(room_info.floor)
    print(room_info.madori)
    print(room_info.area)
    print(room_info.old)
    print(room_info.direction)
    print(room_info.made_of)

get_room_info(input())