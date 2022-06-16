# import requests as r
# import slack_sdk
# from slacker import Slacker
# from pandas.io.json import json_normalize
# import pandas
#
# slack_token = "xoxb-1727525807426-1720771606966-LZ2soxKqJbdEBrinFhYofwGz"
# channel_name = "lyrics"
#
# """
# 현재 문제 :
# 슬랙 봇 작동 안됨
# 슬랙커, 슬랙sdk 모듈 작도 안됨
# open api json형식으로 받기 성공
# """
#
#
# def PostMessage():
#     slack = Slacker(slack_token)
#     slack.chat.post_message(channel_name, "test")
#
#
# def CheckId():
#     url = "https://slack.com/api/conversations.list"
#     para_dict = {
#         "Content-Type": "application/x-www-form-urlencoded",
#         "token": slack_token
#     }
#
#     response = r.get(url=url, params=para_dict)
#     channel_list = pandas.json_normalize(response.json()["channels"])
#     channel_id = list(
#         channel_list.loc[channel_list["name"] == channel_name, "id"])[0]
#
#     print(f"""
#     채널 이름: {channel_name}
#     채널 id: {channel_id}
#     """)
#
#
# def CheckTsnumber():
#     test_text = "sleep nightoff"
#     channel_id = "C01MS4HJMTK"
#     url = "https://slack.com/api/conversations.history"
#     para_dict = {
#         "Content-Type": "application/x-www-form-urlencoded",
#         "token": slack_token,
#         "channel": channel_id
#     }
#
#     response = r.get(url=url, params=para_dict)
#     print(response.json())
#     chat_data = pandas.json_normalize(response.json()["messages"])
#     chat_data['text'] = chat_data['text'].apply(
#         lambda x: x.replace("\xa0", " "))
#     ts = chat_data.loc[chat_data['text'] == test_text, 'ts'].to_list()[0]
#
#     print(f"""
#     글 내용: {test_text}
#     ts: {ts}
#     """)
#
#
# def SendMessage():
#     message = "Sample message"
#     channel_id = "C01MS4HJMTK"
#     ts = "1614419786.001000"
#     url = "https://slack.com/api/chat.postMessage"
#     para_dict = {
#         "Content-Type": "application/x-www-form-urlencoded",
#         "token": slack_token,
#         "channel": channel_id,
#         "text": message,
#         "reply_broadcast": "True",
#         "thread_ts": ts
#     }
#
#     response = r.post(url=url, params=para_dict)
#
# # print(res.status_code)
# # # print(res.text)
# # result = res.json()
# # print(result)
# # print(type(result))
# #
# # # print(result["arvlMsg2"])
# # print(result['errorMessage'])
#
#
# # CheckId()
# SendMessage()

