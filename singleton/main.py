# client


from singleton_logger import SingletonLogger


def main():
    singleton1 = SingletonLogger.get_instance()
    # singleton2 = SingletonLogger()
    singleton2 = SingletonLogger.get_instance()

    if singleton1 is singleton2:
        print("same instance, correct!")

    singleton2.log("singleton pattern example")


if __name__ == "__main__":
    main()
