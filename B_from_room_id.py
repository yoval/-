import requests, re, time, json, threading

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',    
    'Host': 'api.live.bilibili.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
        }


def get_medal(RoomID):
    R_url = 'https://api.live.bilibili.com/live_user/v1/UserInfo/get_anchor_in_room?roomid=%d'%RoomID
    R_Data = requests.get(R_url,headers =headers).text
    R_Json = json.loads(R_Data)
    try:
        uid =  R_Json['data']['info']['uid']
        LiveLevel=R_Json['data']['level']['master_level']['level']
    except :
        uid ='-'
    if uid !='-':
        U_url = 'https://api.live.bilibili.com/rankdb/v1/RoomRank/webMedalRank?roomid=%d&ruid=%d'%(RoomID,uid)
        U_Data = requests.get(U_url,headers =headers).text
        U_Json = json.loads(U_Data)
        try:
            Medal_Name=U_Json['data']['list'][0]['medal_name']
        except:
            Medal_Name = '-'#有直播间无勋章
        with open('medal.txt','a',encoding = 'utf-8') as f :
            f.writelines(['room_id:',str(RoomID),',','uid:',str(uid),',medal_name:',str(Medal_Name),',','livelevel:',str(LiveLevel),'\n'])

def main():
    threads = []
    threadsNum=10
    for i in range(0,threadsNum):
        threads.append(threading.Thread())
    RoomID = 1000 ##起始房间号
    while RoomID<23000000: ##终止房间号
        for i in range(0,threadsNum): 
            if threads[i].isAlive()==False:
                threads[i]=threading.Thread(target=get_medal,args=(RoomID,))
                threads[i].start()
                RoomID+=1
    print('超时等待')
    sleep(30) ##超时等待
    
if __name__ == "__main__":

    main()
	requests.get('https://sc.ftqq.com/SCU34618T5523f49bf9a1230adb8d25855278a9215bcef07fc5680.send?text=B站勋章脚本运行完成')