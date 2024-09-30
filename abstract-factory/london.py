from capital_city import CapitalCity

# concrete product b1
class London(CapitalCity):
    def get_population(self) -> int:
        return 9000000
    
    def list_top_attractions(self) -> []:
        return ['a','b']