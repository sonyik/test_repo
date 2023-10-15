class Human:
    def __init__(self, age, name) -> None:
        self.age = age
        self.name = name

class Slave(Human):
    def __init__(self, status, age, name) -> None:
        super().__init__(age, name)
        self.age = age
        self.name = name
        self.status = status

class Nigger(Slave):
    def __init__(self, status, age, name, is_nigger) -> None:
        super().__init__(status, age, name)
        self.is_nigger = is_nigger
        self.age = age
        self.name = name
        self.status = status
    def get_name(self):
        return print(self.name)

NIGREEGRERSE = Nigger("alive", 12, "uebishe", "YEEES")
NIGREEGRERSE.get_name()