from abc import ABC
from typing import override
from compounding import Compounding
from .vehicle import Vehicle


class Loan(Vehicle, ABC):

    def __init__(self, rate: Compounding, principle: float):
        super().__init__(rate, -principle)

    @override
    def invest(self, amount: float):
        """
        Pay off the outstanding balance by `amount`\n
        Raises `LoanTerminatedException` if `amount` is greater than the outstanding balance
        """
        if amount > abs(self._current_value):
            self._current_value = 0
            amount_leftover = amount-abs(self._current_value)
            self._current_value = 0
            raise LoanTerminatedException(amount_leftover)
        super().invest(amount)
    
class LoanTerminatedException(Exception):

    def __init__(self, remaining_amount: float, *args):
        super().__init__(*args)
        self.remaining = remaining_amount
