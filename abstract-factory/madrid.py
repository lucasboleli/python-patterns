from capital_city import CapitalCity

# concrete product b2
class Madrid(CapitalCity):
    def get_population(self) -> int:
        return 5000000
    
    def list_top_attractions(self) -> []:
        return ['c','d']