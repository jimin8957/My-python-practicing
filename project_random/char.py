import possibility


class gamble:
    def __init__(self, name):
        self.health = 200
        self.damage = 0
        self.name = str(name)
        self.heal = 0

    def __str__(self):
        return "{}의 체력은 {}, 공격은 {}".format(self.name, self.health, self.damage)

    def sk_1(self):
        if possibility.ninety() == True:
            self.damage = 15
        else:
            self.damage = 0

    def sk_2(self):
        if possibility.seventy() == True:
            self.damage = 35
        else:
            self.damage = 0

    def sk_3(self):
        if possibility.forty() == True:
            self.damage = 80
        else:
            self.damage = 0

    def sk_4(self):
        if possibility.fifteen() == True:
            self.damage = 120
        else:
            self.damage = 0

    def special(self):
        if possibility.ten() == True:
            self.damage = 1000
        else:
            self.damage = 0


class tank:
    def __init__(self, name):
        self.health = 300
        self.damage = 0
        self.name = str(name)
        self.heal = 0

    def __str__(self):
        return "{}의 체력은 {}".format(self.name, self.health, self.damage)

    def sk_1(self):
        if possibility.ninety() == True:
            self.damage = 25
        else:
            self.damage = 0

    def sk_2(self):
        if possibility.seventy() == True:
            self.damage = 30
        else:
            self.damage = 0

    def sk_3(self):
        if possibility.fifty() == True:
            self.damage = 45
        else:
            self.damage = 0

    def sk_4(self):
        if possibility.thirty() == True:
            self.damage = 55
        else:
            self.damage = 0

    def special(self):
        self.heal = 40

