from language import Language

#concrete product A1
class English(Language):
    def greet(self) -> str:
        return 'hi'