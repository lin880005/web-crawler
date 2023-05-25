import requests
import json
import time
import jieba
import operator

token ="EAACrso8j7fEBADSwT7XqSEcEUqxICS77FwxfLOEDJERDANZAMYBTBh4UJyZBTbZAmfoFvqbyybStck5nPcatlEuu6QI96HlFlyNcs8pr59JZAb5tG9pJFWPOcElQZB2ZBgYKGogcSJO00hKbbxtt3ZBxPAf8M2R57GvJeCmIAqF5HvoiKubLqEVk0ZCmvL4vlzErmxHOsNqoOQZDZD"
res = requests.get("https://graph.facebook.com/v16.0/me/posts?access_token="+token)
jd = json.loads(res.text)
corpus =[]
page = 0
while jd["data"] != []:  #最後一頁是空list，所以while!=[]繼續做下去
    for list in jd["data"]: #內迴圈抓重複抓資料印出來
        if "message" in list:
            #print(list["message"])
            corpus += jieba.lcut(list["message"])
            

    res = requests.get(jd["paging"]["next"])
    page+=1
    time.sleep(3)
    print(f"============================{page}==============================")
    jd=json.loads(res.text)
#print(corpus)

dic = {}
for list in corpus:
    if list in dic:
        dic[list] += 1
    else:
        dic[list] = 1

#print(dic)
sor = sorted(dic.items(),key=operator.itemgetter(1),reverse=True) 
print(sor)




