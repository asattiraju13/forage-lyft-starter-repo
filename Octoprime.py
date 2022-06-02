from tire import Tire

class Octoprime(Tire):
    def __init__(self, worn_array):
        self.worn_array = worn_array

    def needs_service(self):
        return sum(self.worn_array) >= 3