
# -*- coding:utf-8 -*-
from requests import post
from json import loads


def tuling(info, user_id):
    url = "http://www.tuling123.com/openapi/api"
    with open("tuling123.key") as fp:
        key=fp.readline()
    json_payload = {"key": key,
                    "info": info,
                    "userid": user_id
                    }
    ans = post(url, json_payload)
    text = loads(ans.content.decode("utf-8"))
    if 'url' in text.keys():
        return text['text']+'\n'+text['url']
    else:
        return text['text']


if __name__ == "__main__":
    res = tuling("沪深指数", "123456")
    print(res)