class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        self.name = name
        self._password = password
        self._payment_limit = payment_limit

    @property
    def password(self):
        return "비번 공개 불가"

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def payment_limit(self):
        return self._payment_limit

    @payment_limit.setter
    def payment_limit(self, limit):
        if limit < 0 or limit > self.MAX_PAYMENT_LIMIT:
            print("한도 초과")
        else:
            self._payment_limit = limit


card = CreditCard("강영훈", "123", 100000)
print(card.name)
print(card.password)
print(card.payment_limit)

card.name = "성태호"
card.password = "1234"
card.payment_limit = -10
print(card.name)
print(card.password)
print(card.payment_limit)