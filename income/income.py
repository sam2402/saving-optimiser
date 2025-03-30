from constants import INTEREST_RATE
from portfolio import Portfolio
import time_tracker

class Income:

    def __init__(self, portfolio: Portfolio):
        self._portfolio = portfolio

    def pass_month(self) -> int:
        gross_monthly_income = Salary.get_current_gross_monthly_income()
        gross_monthly_income_after_compulsory_pre_tax_payments = self._portfolio.make_obligatory_pre_tax_payments(gross_monthly_income)
        return gross_monthly_income * (15_000/90_000)
        
        # get gross income for month - Done
        # pay student loan - Done
        # get gross income minus student loan - Done
        # make pension payment
        # get net income
        # pay rent / mortgage
        # pay living costs
        # return available
        pass
    
class Salary:

    starting_salary = 90_000

    @staticmethod
    def get_current_gross_monthly_income() -> int:
        return Salary._get_current_gross_yearly_income()/12

    @staticmethod
    def _get_current_gross_yearly_income() -> int:
        return (Salary.starting_salary * ((1+INTEREST_RATE)**time_tracker.current_year_index())) + (7000*time_tracker.current_year_index())
