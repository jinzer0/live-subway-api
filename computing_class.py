import requests as r


def get_info(statname: str, direct: int):

    response = r.get(
        f"http://swopenapi.seoul.go.kr/api/subway/4f6f6d4f4766663732374d54754153/json/realtimeStationArrival/0/5/{statname}")
    result = response.json()
    print(result)

    if result["code"].split("-")[1] == '200':
        msg = "도착 정보 없음"
        return msg
    elif result["code"].split("-")[1] == "000":
        msg = f"""> 업데이트 일시 :
    `{result["realtimeArrivalList"][direct]["recptnDt"].split(" ")[1].replace(".0", "")}`
    > 기차 방향 :
    `{result["realtimeArrivalList"][direct]["trainLineNm"]}`
    > 도착 예정 시간 :
    `{int(result["realtimeArrivalList"][direct]["barvlDt"]) / 60}분`
    > 열차 위치 :
    `{result["realtimeArrivalList"][direct]["arvlMsg3"]}`"""
    return msg_0, msg_2


while 1:
    station = input("역명을 입력하세요 (예: 건대입구역, 성수역) : ")
    result = get_info(station, 0)
    print(result)


#TODO 1. get_info로 받은 내용 에러 캐치
# 2. 내용 2개 출력 상행 하행
# 3. 도착 시간 실시간 갱신(매 10초)
# 4. 역 여러개 추가, 삭제할 수 있게