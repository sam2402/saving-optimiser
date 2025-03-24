from datetime import datetime, timedelta
from .loan import Loan


class StudentLoan(Loan):

    def __init__(self):
        super().__init__(0.07, 61_415)
        self._current_date = datetime.now()
        self._expiry_date = datetime(day=1, month=4, year=2055)

    @property
    def current_value(self) -> int:
        return self._current_value
    
    def pass_month(self):
        super().pass_month()
        self._current_date += timedelta(days=30)
        if self._current_date > self._expiry_date:
            self.current_value = 0