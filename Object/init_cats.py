class Cat:
    def __init__(self, name, color='흰색'):
        self.name = name
        self.color = color

    def meow(self):
        print('내 이름은 {}, 색깔은 {}, 야옹 야옹'.format(self.name, self.color))

nabi = Cat("나비")
nabi.meow()
nero = Cat("네로","검은색")
nero.meow()
mimi = Cat("미미", "갈색")
mimi.meow()