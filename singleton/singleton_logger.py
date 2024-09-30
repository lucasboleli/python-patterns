class SingletonLogger:
    _instance = None

    def __init__(self) -> None:
        raise RuntimeError("this is a Singleton, use get_instance")

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = cls.__new__(cls)  # __new__ is called before __init__

        return cls._instance

    def log(self, ex: Exception):
        print(ex)

    def log(self, message: str):
        print(message)
