from user import User


class Alarm:

    def __init__(self) -> None:
        self.beep = False
        self.sleepers = []

    def add_user(self, user: User):
        self.sleepers.append(user)

    def alarm_state(self):
        return self.beep

    def ring(self):
        self.beep = True
        for sleeper in self.sleepers:
            sleeper.update()

        self.sleepers = []
