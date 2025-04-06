from compounding import inflation
from constants import STARTING_SALARY, SAVING_RATIO, YEARLY_SALARY_INCREASE
from portfolio import Portfolio
import time_tracker

class Income:

    def __init__(self, portfolio: Portfolio):
        self._portfolio = portfolio

    def pass_month(self) -> float:
        gross_monthly_income = Salary.get_current_gross_monthly_income()
        compulsory_pre_tax_payments = self._portfolio.make_obligatory_pre_tax_payments(gross_monthly_income)
        # make pension payment
        # get net income
        # pay rent / mortgage
        # pay living costs
        # return available
        return (gross_monthly_income-compulsory_pre_tax_payments) * SAVING_RATIO
    
class Salary:

    starting_salary = STARTING_SALARY

    @staticmethod
    def get_current_gross_monthly_income() -> float:
        return Salary._get_current_gross_yearly_income()/12

    @staticmethod
    def _get_current_gross_yearly_income() -> int:
        return inflation.compound(Salary.starting_salary, False) + (YEARLY_SALARY_INCREASE*time_tracker.current_year_index())
