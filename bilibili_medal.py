# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 10:49:36 2018

@author: fuwen
"""
import requests
import re
import time
import json
import threading


threadsNum = input('threadsNum:')
threadsNum = int(threadsNum)

def get_medal(RoomID):
    UidUrl = 'https://api.live.bilibili.com/live_user/v1/UserInfo/get_anchor_in_room?roomid=%d' % RoomID
    #UidData = requests.get(UidUrl).content
    UidData = requests.get(UidUrl).text
    print(RoomID)
    try:
        Uid = json.loads(UidData)['data']['info']['uid']
        url = 'https://api.live.bilibili.com/rankdb/v1/RoomRank/webMedalRank?roomid=%d&ruid=%d' % (RoomID,Uid)
        #data = requests.get(url).content #windows
        data = requests.get(url).text #lunix
        medal_name = json.loads(data)['data']['list'][0]['medal_name']
    except Exception :
        medal_name = 0
    if(medal_name):
        with open('medal_name.txt','a') as f :
            f.writelines([str(RoomID),',',str(medal_name),'\n'])
        


def main():
    ##创建线程池
    threads = []
#    threadsNum=10
    for i in range(0,threadsNum):
        threads.append(threading.Thread())

    RoomID=1000 ##起始房间号
    while RoomID<1000000: ##终止房间号
        for i in range(0,threadsNum): 
            if threads[i].isAlive()==False:
                threads[i]=threading.Thread(target=get_medal,args=(RoomID,))
                threads[i].start()
                RoomID+=1
    print('超时等待')
    sleep(30) ##超时等待


if __name__ == "__main__":
    main()
