# 클래스 상속

class Vehicle:
    name = '탈것'
    color = '색상'

    def __init__(self,color = None) -> None:
        self.color = color
        print(f'{self.color}색 {self.name} 생성!')


    def desc(self):
        print(f'{self.name} 객체')

    def move(self):
        print(f'{self.name} 이동')

class Car(Vehicle):  # vehicle클래스를 상속받은 Car
    name = '자동차'
    brand = '현대'

    def __init__(self, color=None) -> None:
        super().__init__(color)
        print(f'{color}색 {self.brand},{self.name} 생성!')

    def move(self):
        # print(f'{self.name} 달린다')
        super().move()       #부모 상속으로 쓸때 super().move()
        print(f'{self.name}')
    

    def stop(self):
        print('브레이크로 멈춤')


if __name__ == '__main__':
    vcl = Vehicle('검은')
    vcl.desc()
    vcl.move()


    mycar= Car('흰')
    mycar.desc()
    mycar.move()
    mycar.stop()