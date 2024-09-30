from observer import Observer


class User(Observer):
    def __init__(self) -> None:
        self.awake = False

    def is_awake(self):
        return self.awake

    def update(self):
        print("im awake now")
        self.awake = True
