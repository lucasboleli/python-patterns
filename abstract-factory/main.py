from england_factory import EnglandFactory
from spain_factory import SpainFactory
from country import Country
from international_provider import InternationalProvider

#client
def main():
    country = Country.SPAIN
    factory = InternationalProvider().create(country)
    language = factory.create_language()
    capital_city = factory.create_capital()

    print(f'country {country.name}')
    print(language.__class__.__name__)
    print(language.greet())
    print(capital_city.__class__.__name__)
    print(capital_city.get_population())
    print(capital_city.list_top_attractions())

if __name__ == "__main__":
    main()