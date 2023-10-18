class Krestyanin:
    def __init__(self, age, name) -> None:
        self.age = age
        self.name = name

class Kypec(Krestyanin):
    def __init__(self, status, age, name) -> None:
        super().__init__(age, name)
        self.age = age
        self.name = name
        self.status = status

class Dvoryanin(Kypec):
    def __init__(self, status, age, name, is_bogach) -> None:
        super().__init__(status, age, name)
        self.is_bogach = is_bogach
        self.age = age
        self.name = name
        self.status = status
    def get_name(self):
        return print(self.name)

Boris = Dvoryanin("alive", 12, "Boris", "YEEES")
Boris.get_name()