from tire import Tire

class Carrigan(Tire):
    def __init__(self, worn_array):
        self.worn_array = worn_array

    def needs_service(self):
        return max(self.worn_array) >= 0.9