from typing import Dict, List

class PropertyFilter:
    def __init__(self, year: str = None, city: str = None, status: str = None):
        self.year = year
        self.city = city
        self.status = status

class PropertyResponse:
    def __init__(self, address: str, city: str, price: float, description: str, status: str):
        self.address = address
        self.city = city
        self.price = price
        self.description = description
        self.status = status

    def to_dict(self) -> Dict:
        return {
            'address': self.address,
            'city': self.city,
            'price': self.price,
            'description': self.description,
            'status': self.status
        }

def format_properties(properties: List[Dict]) -> List[PropertyResponse]:
    return [PropertyResponse(**prop) for prop in properties]