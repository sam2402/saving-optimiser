from abc import ABC
from .vehicle import Vehicle


class Loan(Vehicle, ABC):

    def __init__(self, annual_interest_rate: float, principle: int):
        super().__init__(annual_interest_rate, -principle)

    def invest(self, amount: int):
        """
        Pay off the outstanding balance by `amount`\n
        Raises `LoanTerminatedException` if `amount` is greater than the outstanding balance
        """
        print(amount, self._current_value)
        if amount > abs(self._current_value):
            self._current_value = 0
            amount_leftover = amount-abs(self._current_value)
            self._current_value = 0
            raise LoanTerminatedException(amount_leftover)
        super().invest(amount)
    
class LoanTerminatedException(Exception):

    def __init__(self, remaining_amount: int, *args):
        super().__init__(*args)
        self.remaining = remaining_amount
