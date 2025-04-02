from abc import ABC
from constants import fmt


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
    
    def get_obligatory_pre_tax_payment(self, gross_monthly_income: int) -> int:
        """
        Get the amount you would have to pay into this vehicle if you make `gross_monthly_income` in the current month
        """
        return 0

    def __repr__(self):
        return f"{self.__class__.__name__}: £{fmt(self.current_value)}"