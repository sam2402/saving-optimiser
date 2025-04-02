from datetime import datetime, timedelta
from typing import override
from constants import CURRENT_STUDENT_LOAN_MONTHLY_THRESHOLD, DAYS_IN_YEAR, INFLATION_RATE
from .loan import Loan
import time_tracker


class StudentLoan(Loan):
    """
    Plan 2 student loan
    """

    initial_monthly_threshold = CURRENT_STUDENT_LOAN_MONTHLY_THRESHOLD
    cancellation_period = timedelta(days=DAYS_IN_YEAR*30)

    @staticmethod
    def april_after_graduation(date: datetime) -> datetime:
        year = date.year if date.month < 4 else date.year + 1
        return datetime(year=year, month=4, day=1)
        
    def __init__(self, annual_interest_rate: float, principle: int, graduation_date: datetime):
        super().__init__(annual_interest_rate, principle)
        self._expiry_date = StudentLoan.april_after_graduation(graduation_date) + self.cancellation_period
    
    @override
    def pass_month(self):
        super().pass_month()
        if time_tracker.current_date > self._expiry_date:
            self._current_value = 0
    
    @override
    def get_obligatory_pre_tax_payment(self, gross_monthly_income: int) -> int:
        current_monthly_threshold = StudentLoan.initial_monthly_threshold*(1+INFLATION_RATE**time_tracker.current_year_index())
        return (gross_monthly_income-current_monthly_threshold)*0.09