# class User:
#     def say_hello(self):
#         print("안녕, {}이다".format(self.name))
#
#     def login(self, my_email, my_password):
#         if(self.email == my_email and self.password == my_password):
#             print("성공")
#         else:
#             print("실패")
#
# user1 = User()
#
# user1.name = "park"
# user1.email = "jimin"
# user1.password = "1234"
#
# user1.login("jimin", '1234')
# user1.say_hello()
# User.say_hello(user1)
# User.login(user1, "jimin", '1234')

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class Use:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User("Young", "young@codi", "123456")

user2 = Use()
user2.initialize("Lisa", "Lis@codi", "565456")

user3 = Use()
user3.initialize("Young", "young@codi", "123456")

user4 = Use()
user4.initialize("Young", "young@codi", "123456")


print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)