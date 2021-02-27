import requests as r
import slack_sdk
from slacker import Slacker
from pandas.io.json import json_normalize
import pandas

slack_token = "xoxb-1727525807426-1720771606966-LZ2soxKqJbdEBrinFhYofwGz"
channel_name = "lyrics"

"""
현재 문제 : 
슬랙 봇 작동 안됨
슬랙커, 슬랙sdk 모듈 작도 안됨
open api json형식으로 받기 성공
"""


def PostMessage():
    slack = Slacker(slack_token)
    slack.chat.post_message(channel_name, "test")


def CheckId():
    url = "https://slack.com/api/conversations.list"
    para_dict = {
        "Content-Type": "application/x-www-form-urlencoded",
        "token": slack_token
    }

    response = r.get(url=url, params=para_dict)
    channel_list = pandas.json_normalize(response.json()["channels"])
    channel_id = list(channel_list.loc[channel_list["name"] == channel_name, "id"])[0]

    print(f"""
    채널 이름: {channel_name}
    채널 id: {channel_id}
    """)


def CheckTsnumber():
    test_text = "sleep nightoff"
    channel_id = "C01MS4HJMTK"
    url = "https://slack.com/api/conversations.history"
    para_dict = {
        "Content-Type": "application/x-www-form-urlencoded",
        "token": slack_token,
        "channel": channel_id
    }

    response = r.get(url=url, params=para_dict)
    print(response.json())
    chat_data = pandas.json_normalize(response.json()["messages"])
    chat_data['text'] = chat_data['text'].apply(lambda x: x.replace("\xa0", " "))
    ts = chat_data.loc[chat_data['text'] == test_text, 'ts'].to_list()[0]

    print(f"""
    글 내용: {test_text}
    ts: {ts}
    """)


def SendMessage():
    message = """
    점점 좁아지던 골목의 막힌 끝에 서서
외투 위의 먼지를 털다 웃었어
벽에 기대어 앉으며 짐을 내려놓으니
한 줌의 희망이 그토록 무거웠구나
탓할 무언가를 애써 떠올려봐도
오직 나만의 어리석음 뿐이었네
나 조금 누우면 안 될까
잠깐 잠들면 안 될까
날도 저무는데
아무도 없는데
나 조금 누우면 안 될까
이대로 잠들면 안 될까
따뜻한 꿈속에서
조금 쉬고 올 거야
많은 게 달라지고 변하고 시들어 가고
애써 감춰온 나의 지친 마음도
더는 필요 없을 자존심을 내려놓으니
이젠 나 자신을 가엾어해도 되겠지
탓할 무언가를 애써 떠올려봐도
오직 나만의 어리석음 뿐이었네
나 조금 누우면 안 될까
잠깐 잠들면 안 될까
날도 저무는데
아무도 없는데
나 조금 누우면 안 될까
이대로 잠들면 안 될까
따뜻한 꿈속에서
못다한 악수와 건배를 나누며
이제 와 뭘 어쩌겠냐고 웃으며 웃으며
모두 보고 싶다
나 조금 누우면 안 될까
잠깐 잠들면 안 될까
날도 저무는데
아무도 없는데
나 조금 누우면 안 될까
이대로 잠들면 안 될까
따뜻한 꿈속에서
조금 쉬고 올 거야
    """
    channel_id = "C01MS4HJMTK"
    ts = "1614419786.001000"
    url = "https://slack.com/api/chat.postMessage"
    para_dict = {
        "Content-Type": "application/x-www-form-urlencoded",
        "token": slack_token,
        "channel": channel_id,
        "text": message,
        "reply_broadcast": "True",
        "thread_ts": ts
    }

    response = r.post(url=url, params=para_dict)


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
# CheckId()
SendMessage()
