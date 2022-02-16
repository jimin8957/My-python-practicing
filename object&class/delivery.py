class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return ("{} 가격 : {}".format(self.name, self.price))

burger = MenuItem("햄버거", 4000)
coke = MenuItem("콜라", 1500)
fries = MenuItem("후렌치 후라이", 1500)

# print(burger)
# print(coke)
# print(fries)


class SimpleCalculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

# 계산기 인스턴스 생성
calculator = SimpleCalculator()

# # 계산기 연산 호출
# print(calculator.add(4, 5))
# print(calculator.subtract(4, 5))


class GameCharacter:
    # 게임 캐릭터 클래스
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power
        # 게임 캐릭터는 속성으로 이름, hp, 공격력을 갖는다

    def is_alive(self):
        # 게임 캐릭터가 살아있는지(체력이 0이 넘는지) 확인하는 메소드
        return self.hp > 0

    def get_attacked(self, damage):
        if self.hp > 0:
            self.hp -= damage
        else:
            print("{}님은 이미 죽었습니다.".format(self.name))

        """ 
        게임 캐릭터가 살아있으면 공격한 캐릭터의 공격력만큼 체력을 깎는 메소드
        조건:    
            1. 이미 캐릭터가 죽었으면 죽었다는 메시지를 출력한다
            2. 남은 체력보다 공격력이 더 크면 체력은 0이 된다.
        """

    def attack(self, other_character):
        # 게임 캐릭터가 살아있으면 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다.
        other_character.get_attacked(self.power)

    def __str__(self):
        # 게임 캐릭터의 의미있는 정보를 포함한 문자열을 리턴한다.
        return (f"{self.name}님의 hp는 {self.hp}만큼 남았습니다.")


# # 게임 캐릭터 인스턴스 생성
# character_1 = GameCharacter("Ww영훈전사wW", 200, 30)
# character_2 = GameCharacter("Xx지웅최고xX", 100, 50)
#
# # 게임 캐릭터 인스턴스들 서로 공격
# character_1.attack(character_2)
# character_2.attack(character_1)
# character_2.attack(character_1)
# character_2.attack(character_1)
# character_2.attack(character_1)
# character_2.attack(character_1)
#
# # 게임 캐릭터 인스턴스 출력
# print(character_1)
# print(character_2)

class Post:
    # 게시글 클래스
    def __init__(self, date, content):
        # 게시글은 속성으로 작성 날짜와 내용을 갖는다
        self.date = date
        self.content = content

    def __str__(self):
        # 게시글의 정보를 문자열로 리턴하는 메소드
        return "게시일: {}\n내용: {}".format(self.date, self.content)

class BlogUser:
    def __init__(self, name):
        self.name = name
        self.posts = []

    def add_post(self, date, content):
        new_post = Post(date, content)
        self.posts.append(new_post)

    def show_all_posts(self):
        for post in self.posts:
            print(post)

    def __str__(self):
        return "안녕하세요 {}입니다.\n".format(self.name)

# 블로그 유저 인스턴스 생성
blog_user_1 = BlogUser("성태호")

# 블로그 유저 인스턴스 출력(인사, 이름)
print(blog_user_1)

# 블로그 유저 게시글 2개 추가
blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이였다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")

# 블로그 유저의 모든 게시글 출력
blog_user_1.show_all_posts()