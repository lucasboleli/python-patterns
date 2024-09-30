from capital_city import CapitalCity
from language import Language
from international_factory import InternationalFactory
from spanish import Spanish
from madrid import Madrid

#concrete factory 2
class SpainFactory(InternationalFactory):
    def create_language(self) -> Language:
        return Spanish()
    
    def create_capital(self) -> CapitalCity:
        return Madrid()