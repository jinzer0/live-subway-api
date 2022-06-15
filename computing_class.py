import requests as r


def get_info(statname: str, direct: int):
    response = r.get(
        f"http://swopenapi.seoul.go.kr/api/subway/4f6f6d4f4766663732374d54754153/json/realtimeStationArrival/0/5/{statname}")
    result = response.json()
    print(result)
#     msg = f"""> 업데이트 일시 :
# `{result["realtimeArrivalList"][direct]["recptnDt"].split(" ")[1].replace(".0", "")}`
# > 기차 방향 :
# `{result["realtimeArrivalList"][direct]["trainLineNm"]}`
# > 도착 예정 시간 :
# `{int(result["realtimeArrivalList"][direct]["barvlDt"]) / 60}분`
# > 열차 위치 :
# `{result["realtimeArrivalList"][direct]["arvlMsg3"]}`"""
    return msg


print(get_info("오목교(목동운동장앞)", 0))
