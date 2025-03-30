from datetime import datetime, timedelta
from typing import override
from constants import DAYS_IN_MONTH, INTEREST_RATE
from .loan import Loan
import time_tracker


class StudentLoan(Loan):

    initial_monthly_threshold = 2274
  
    def __init__(self):
        super().__init__(INTEREST_RATE+0.03, 61_415)
        self._current_date = datetime.now()
        self._expiry_date = datetime(day=1, month=4, year=2055)
    
    @override
    def pass_month(self):
        super().pass_month()
        self._current_date += timedelta(days=DAYS_IN_MONTH)
        if self._current_date > self._expiry_date:
            self.current_value = 0
    
    @override
    def get_obligatory_pre_tax_payment(self, gross_monthly_income: int) -> int:
        current_monthly_threshold = StudentLoan.initial_monthly_threshold*(1+INTEREST_RATE**time_tracker.current_year_index())
        return (gross_monthly_income-current_monthly_threshold)*0.09