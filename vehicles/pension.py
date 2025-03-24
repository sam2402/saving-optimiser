from .vehicle import Vehicle

class Pension(Vehicle):

    def __init__(self):
        super().__init__(0.05)