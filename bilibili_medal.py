# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 10:49:36 2018

@author: fuwen
"""
import requests
import re
import time
import json

def get_medal(RoomID):
    UidUrl = 'https://api.live.bilibili.com/live_user/v1/UserInfo/get_anchor_in_room?roomid=%d' % RoomID
    UidData = requests.get(UidUrl).content
    Uid = json.loads(UidData)['data']['info']['uid']
    url = 'https://api.live.bilibili.com/rankdb/v1/RoomRank/webMedalRank?roomid=%d&ruid=%d' % (RoomID,Uid)
    data = requests.get(url).content
    medal_name = json.loads(data)['data']['list'][0]['medal_name']
    print(medal_name)
    return Uid,medal_name

for RoomID in range(4028602,5000000):
    print(RoomID)
    try:
        Uid,medal_name = get_medal(RoomID)
        with open('medal_name.txt','a') as f :
            f.writelines([str(RoomID),',',str(medal_name),'\n'])
    except Exception as e:
        pass



