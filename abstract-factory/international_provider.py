from country import Country
from england_factory import EnglandFactory
from spain_factory import SpainFactory
from international_factory import InternationalFactory

#provider
class InternationalProvider:
    @staticmethod
    def create(country: Country) -> InternationalFactory:
        match country:
            case Country.ENGLAND:
                return EnglandFactory()
            case Country.SPAIN:
                return SpainFactory()
            case _:
                return "county not supported"