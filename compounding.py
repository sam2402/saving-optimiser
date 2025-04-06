from math import prod
from constants import INFLATION_RATE, SIMULATION_YEARS
import time_tracker

class Compounding:

    def __init__(self, rate: float):
        self.rates = [1+rate]*(SIMULATION_YEARS+1)
    
    @property
    def _total_compound_factor_to_current_year_start(self) -> float:
        return prod(self.rates[:time_tracker.current_year_index()])
    
    @property
    def _compound_factor_during_current_year(self) -> float:
        return (self.current_yearly_rate)**((time_tracker.current_month_index%12)/12)

    @property
    def current_yearly_rate(self):
        return self.rates[time_tracker.current_year_index()]
    
    @property
    def current_monthly_rate(self):
        return (self.rates[time_tracker.current_year_index()])**(1/12)
    
    def compound(self, amount: float, account_for_months_in_current_year = True) -> float:
        """If amount was invested at t=0, return how much would it have compounded to now"""
        factor = \
            self._total_compound_factor_to_current_year_start * (
                self._compound_factor_during_current_year if account_for_months_in_current_year else 1
            )
        return amount * factor

class Inflation(Compounding):

    def __init__(self, rate: float):
        super().__init__(rate)

    def adjusted(self, amount: float, account_for_months_in_current_year = True) -> float:
        """If how much is `amount` worth in t=0 dollars (at the start of the simulation)"""
        factor = self._total_compound_factor_to_current_year_start * (
                self._compound_factor_during_current_year if account_for_months_in_current_year else 1
            )
        return amount / factor

inflation = Inflation(INFLATION_RATE)

