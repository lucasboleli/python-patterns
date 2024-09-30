from alarm import Alarm
from user import User


def main():
    alarm = Alarm()
    user = User()
    user2 = User()

    alarm.add_user(user)
    alarm.add_user(user2)
    alarm.ring()


if __name__ == "__main__":
    main()
