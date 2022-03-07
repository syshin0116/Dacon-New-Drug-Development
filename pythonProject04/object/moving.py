class Car:
    # member변수
    color = ''
    shape = ''

    # member함수
    def speed_up(self):
        print(self.color + '색인 자동차의 속도를 up!')

    def speed_down(self):
        print('자동차의 속도를 down!')

    def __str__(self):
        return self.color + ', ' + self.shape
