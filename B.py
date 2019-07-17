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

def get_medal(uid):
    url = 'https://api.live.bilibili.com/live_user/v1/Master/info?&uid=%d'%uid
    try:
        MedalData = requests.get(url,headers =headers).text
    except Exception as e:
        try:
            time.sleep(5)
            MedalData = requests.get(url,headers =headers).text
        except Exception as e:
            with open('error.txt','a') as g:
                g.writelines(['uid:',str(uid),'\n'])
    MedalJson = json.loads(MedalData)
    try:
        if MedalJson['data']['medal_name']:
            medal_name = MedalJson['data']['medal_name']
            room_id = MedalJson['data']['room_id']
            with open('medal_name.txt','a',encoding = 'utf-8') as f :
                f.writelines(['uid:',str(uid),',','room_id:',str(room_id),',','medal_name:',str(medal_name),'\n'])
    except Exception as e:
        pass


def main():
    threads = []
    threadsNum=10
    for i in range(0,threadsNum):
        threads.append(threading.Thread())

    uid = 1290222 ##起始房间号
    while uid<5000000: ##终止房间号
        for i in range(0,threadsNum): 
            if threads[i].isAlive()==False:
                threads[i]=threading.Thread(target=get_medal,args=(uid,))
                threads[i].start()
                uid+=1
    print('超时等待')
    sleep(30) ##超时等待
    
if __name__ == "__main__":

    main()
