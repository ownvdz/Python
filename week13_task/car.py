# 202344053, 김유현
import datetime

class Car:
    def __init__(self, number) -> None:
        self.number = number # 차량번호
        self.intime = datetime.datetime.now() # 입차시간
        self.outtime = None # 출차시간

    def set_out(self):
        # 출차시 호출하는 메소드
        # 현재 메소드가 호출한 시간으로
        # 출차 시간을 설정한다.
        self.outtime = datetime.datetime.now()

    def is_out(self):
        # self.outtime 이 None 인지 아닌지 판별해서
        # 출차를 했는지 여부를 True, False 로 반환한다.
        if self.outtime:
            return True
        
        return False

    def cal_price(self, hour=2000):
        # 출차를 하지 않은 경우에는 현재 시간까지의 주차 요금을 계산하고
        # 출차를 한 경우에는 출차한 시간을 기준으로 주차 요금을 계산한다.
        # 시간당 2000 원이며, 다른 요금을 적용하고 싶으면 원하는 시간당 요금을 사용할 수 있도록 한다.
        # 두 시간 차이를 구하고 total_seconds()을 이용하면
        # 두 시간 차이를 초 단위로 얻을 수 있다.
        # 이를 이용하여 주차 요금을 계산한다.
        # 계산한 주차 요금을 반환한다.
        if self.is_out():
            return datetime.timedelta.total_seconds(self.outtime-self.intime)/3600*hour

    def __str__(self) -> str:
        # 차량 번호와 입차시간 출차시간을 적절하게 문자열로 조합해서 반환한다.
        # 단 출차를 하지 않은 경우에는 출차시간 대신 '주차중'이라고 표시한다
        # 입차시간과 출차시간을 문자열로 바꾸는 방법은
        # 13 주차_연습예제.pdf p.5 [날짜시간 <->문자열]의
        # 5 번 strftime()을 이용하면 된다.
        # 교재 p.412 참조
        if self.outtime:
            return f"{self.number}, {datetime.datetime.strftime(self.intime)}, {datetime.datetime.strftime(self.outtime)}"
        
        return "주차중"