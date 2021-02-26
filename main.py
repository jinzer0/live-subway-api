import requests as r
import slack_sdk
from slacker import Slacker

slack_token = "xoxb-1727525807426-1720771606966-LZ2soxKqJbdEBrinFhYofwGz"
channel_name = "lyrics"
url = "https://slack.com/api/conversations.list"
params = {
    "Content-Type": "application/x-www-form-urlencoded",
    "token": slack_token
}
"""
현재 문제 : 
슬랙 봇 작동 안됨
슬랙커, 슬랙sdk 모듈 작도 안됨
open api json형식으로 받기 성공
"""


# s_res = r.get(url=url, params=params)
# print(s_res.json())
# s_res_data = s_res.json()
# print(s_res_data["ok"])

def PostMessage():
    slack = Slacker("xoxb-1727525807426-1720771606966-Uvd1Xqa7pwrcEXamvUKRoGw4")
    slack.chat.post_message(channel_name, "hel")

# response = r.get(
#     "http://swopenapi.seoul.go.kr/api/subway/4f6f6d4f4766663732374d54754153/json/realtimeStationArrival/0/5/목동")
# print(res.status_code)
# # print(res.text)
# result = res.json()
# print(result)
# print(type(result))
#
# # print(result["arvlMsg2"])
# print(result['errorMessage'])


# slack message 필요
