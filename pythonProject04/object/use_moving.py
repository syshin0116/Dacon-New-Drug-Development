import object.moving as m #module까지

if __name__ == '__main__':
    # class의 instance인 object!
    c1 = m.Car() # new Car()
    c1.shape = '네모'
    c1.color = 'red'
    c2 = m.Car()
    c2.shape = '세모'
    c2.color = 'green'
    # print(c1)
    # print(c2)
    c1.speed_up()
    c2.speed_down()