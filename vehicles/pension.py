from typing import override
from compounding import Compounding
from income.income import Salary
from .vehicle import Vehicle

class Pension(Vehicle):

    def __init__(self, rate: Compounding, employer_match: float, current_value: float):
        super().__init__(rate, current_value)
        self._employer_match = employer_match
    
    @override
    def invest(self, amount):
        gross_monthly_income = Salary.get_current_gross_monthly_income()
        employer_contribution =  min(amount, gross_monthly_income * self._employer_match)
        super().invest(amount+employer_contribution)