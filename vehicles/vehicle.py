from abc import ABC
from compounding import Compounding
from constants import fmt


class Vehicle(ABC):

    def __init__(self, rate: Compounding, current_value: float = 0):
        self._annual_interest_rate = rate
        self._current_value = current_value

    @property
    def current_value(self) -> float:
        return self._current_value

    def invest(self, amount: float):
        self._current_value += amount

    def pass_month(self):
        self._current_value *= self._annual_interest_rate.current_monthly_rate
    
    def get_obligatory_pre_tax_payment(self, gross_monthly_income: float) -> float:
        """
        Get the amount you would have to pay into this vehicle if you make `gross_monthly_income` in the current month
        """
        return 0

    def __repr__(self):
        return f"{self.__class__.__name__}: {fmt(self.current_value)}"