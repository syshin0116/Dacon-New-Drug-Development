# 새로운 클래스를 만들 때
# 기존의 있던 ㄹ래스를 "재사용!"해서
# 만드는 것을 상속이라고 함.
from object.moving import Car

class Sedan(Car):
    person = 0

    def tour(selfself):
        print('편안하게 여행을 가다')

class Truck(Car):
    #멤버2개, 멤버함수2개
    weight = 0

    def move(self):
        print('짐을 싣고 가다.')