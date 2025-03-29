from abc import ABC


class Vehicle(ABC):

    def __init__(self, annual_interest_rate: float, current_value: int = 0):
        self._annual_interest_rate = annual_interest_rate
        self._current_value = current_value

    @property
    def current_value(self) -> int:
        return self._current_value

    def invest(self, amount: int):
        self._current_value += amount

    def pass_month(self):
        self._current_value *= (1+self._annual_interest_rate)**(1/12)
    
    def __repr__(self):
        return f"{self.__class__.__name__}: {self.current_value}"