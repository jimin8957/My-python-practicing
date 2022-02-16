from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        self.speed = 0

    @property
    @abstractmethod
    def speed(self):
        pass

class Bicycle(Vehicle):
    max_speed = 15

    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0

    def start(self):
        print("자전거 페달 돌리기 시작")
        self.speed = 1/3 * Bicycle.max_speed

    def __str__(self):
        return "이 자전거는 현재 {}km/h로 주행 중".format(self.speed)


class NormalCar(Vehicle):
    def __init__(self, speed, max_speed):
        self._speed = 0
        self.max_speed = max_speed

    def start(self):
        self.speed = 1/2 * self.max_speed
        print("일반 자동차 시동 검")

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0

    def __str__(self):
        return "이 일반자동차는 현재 {}km/h로 주행 중".format(self.speed)


class SportsCar(Vehicle):
    def __init__(self, speed, max_speed):
        self._speed = speed
        self.max_speed = max_speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0

    def start(self):
        self.speed = self.max_speed
        print("스포츠카 시동 검")

    def __str__(self):
        return "이 스포츠카는 현재 {}km/h로 주행 중".format(self.speed)



class DrivingSimulator:
    def __init__(self):
        """교통 수단 인스턴스들을 담을 리스트를 변수로 갖는다"""
        self.vehicles = []

    def add_vehicle(self, new_vehicle):
        """교통 수단 인스턴스들만 시뮬레이터에 추가될 수 있게 한다"""
        if isinstance(new_vehicle, Vehicle):
            self.vehicles.append(new_vehicle)
        else:
            print("{}은 교통 수단이 아니라 추가 불가".format(new_vehicle))

    def start_all_vehicles(self):
        """모든 교통 수단을 주행 시작시킨다"""
        print("모든 교통 수당 주행 시작")
        for veh in self.vehicles:
            veh.start()

    def stop_all_vehicles(self):
        """모든 교통 수단을 주행 정지시킨다"""
        print("모든 교통 수당 주행 정지")
        for veh in self.vehicles:
            veh.stop()

    def __str__(self):
        """갖고 있는 교통 수단들의 현재 속도를 문자열로 리턴한다"""
        res_str = ""

        for veh in self.vehicles:
            res_str += str(veh) + "\n"

        return  res_str

# 자전거 인스턴스
bicycle = Bicycle(0)

# 일반 자동차 인스턴스들
car_1 = NormalCar(0, 100)
car_2 = NormalCar(0, 120)

# 스포츠카 인스턴스들
sports_car_1 = SportsCar(0, 200)
sports_car_2 = SportsCar(0, 190)


# 주행 시뮬레이터 인스턴스
driving_simulator = DrivingSimulator()

# 교통 수단 인스턴스들을 주행 시뮬레이터에 추가한다
driving_simulator.add_vehicle(bicycle)
driving_simulator.add_vehicle(car_1)
driving_simulator.add_vehicle(car_2)
driving_simulator.add_vehicle(sports_car_1)
driving_simulator.add_vehicle(sports_car_2)
driving_simulator.add_vehicle(1)

# 시뮬레이터 내 모든 인스턴스들을 주행 시작시킨다
driving_simulator.start_all_vehicles()
print(driving_simulator)

# 시뮬레이터 내 모든 인스턴스들을 주행 정지시킨다
driving_simulator.stop_all_vehicles()
print(driving_simulator)