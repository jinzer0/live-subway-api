import discord
import requests as r

bot_token = "ODE2OTQyMzQzMjE0NDY1MDY2.YECS2A.-ZEHteB08LRfjOFmGJNTKyi1uwY"
bot_clientID = "816942343214465066"


class MyClient(discord.Client):
    def GetInfo(self, statname, direct):
        response = r.get(
            f"http://swopenapi.seoul.go.kr/api/subway/4f6f6d4f4766663732374d54754153/json/realtimeStationArrival/0/5/{statname}")
        result = response.json()
        msg = f"""> 업데이트 일시 : 
`{result["realtimeArrivalList"][direct]["recptnDt"].split(" ")[1].replace(".0", "")}`
> 기차 방향 : 
`{result["realtimeArrivalList"][direct]["trainLineNm"]}`
> 도착 예정 시간 : 
`{int(result["realtimeArrivalList"][direct]["barvlDt"]) / 60}분`
> 열차 위치 : 
`{result["realtimeArrivalList"][direct]["arvlMsg3"]}`"""
        return msg

    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print("message author : ", message.author, "\nmessage : ", message.content)

        if message.content == "옴교" or message.content == "오목교":
            result = self.GetInfo("오목교(목동운동장앞)", 2)
            await message.channel.send(result)
            await message.delete()
            await message.channel.send("반대 방향의 지하철 정보를 원합니까? [y/n]")

        elif message.content == "ㄱㄷ" or message.content == "고덕":
            result = self.GetInfo("고덕", 0)
            await message.channel.send(result)
            await message.delete()
            await message.channel.send("반대 방향의 지하철 정보를 원합니까? [y/n]")

        else:
            result_1 = self.GetInfo(message.content, 0)
            result_2 = self.GetInfo(message.content, 3)
            await message.channel.send(result_1)
            await message.channel.send(result_2)
            await message.delete()


# result["errorMessage"]["total"] # 데이터 건
# result["errorMessage"]["code"] # 요청 에러 코드
# result["errorMessage"]["message"] # 요청 상태 메세지
# result["realtimeArrivalList"]["trainLineNm"] # 기차 방향 (방화행 ~방면)
# result["realtimeArrivalList"]["barvlDt"] # 열차도착예정시간 단위 : 초
# result["realtimeArrivalList"]["recptnDt"] # 열차도착정보를 생성한 시각
# result["realtimeArrivalList"]["arvlMsg2"] # 첫번째도착메세지
# result["realtimeArrivalList"]["arvlMsg3"] # 두번째도착메세지 - 열차위치
# result["realtimeArrivalList"]["arvlCd"] # 도착코드 // (0:진입, 1:도착, 2:출발, 3:전역출발, 4:전역진입, 5:전역도착, 99:운행중)


myclient = MyClient()
myclient.run(bot_token)
