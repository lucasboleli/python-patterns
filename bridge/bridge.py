from abc import ABC


class Color(ABC):
    def __init__(self) -> None:
        pass


class Red(Color):
    def __init__(self) -> None:
        print("red")


class Blue(Color):
    def __init__(self) -> None:
        print("blue")


class Gear(ABC):
    def __init__(self) -> None:
        pass


class SmallGear(Gear):
    def __init__(self) -> None:
        print("small gear")


class BigGear(Gear):
    def __init__(self) -> None:
        print("big gear")


class Vehicle(ABC):
    def __init__(self) -> None:
        pass

    def set_color(self, color: Color):
        self.color = color

    def set_gear(self, gear: Gear):
        self.gear = gear

    def display(self):
        print("color: ", type(self.color), " gear: ", type(self.gear))


class Car(Vehicle):
    def __init__(self) -> None:
        pass


def main():
    color = Blue()
    gear = BigGear()
    car = Car()
    car.set_color(color)
    car.set_gear(gear)
    car.display()


if __name__ == "__main__":
    main()
