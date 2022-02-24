class Clock:
    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec

    def __str__(self):
        return "{}:{}:{}".format(self.hour, self.min, self.sec)

    def tick(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
        if self.min == 60:
            self.min = 0
            self.hour += 1
        if self.hour == 24:
            self.sec = 0
            self.min = 0
            self.hour = 0

    def set(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec



# 1시 30분 48초인 시계 인스턴스 생성
clock = Clock(1, 30, 48)

print(clock)

# 13초를 늘린다
for i in range(13):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)

# 2시 3분 58초로 시계 세팅
clock.set(2, 3, 58)

# 5초를 늘린다
for i in range(5):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)

# 23시 59분 57초로 세팅
clock.set(23, 59, 57)

# 5초를 늘린다
for i in range(5):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)