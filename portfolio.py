from typing import Iterable, Optional
from constants import fmt
from investment_matrix import InvestmentMatrix
from vehicles.loan import LoanTerminatedException
from vehicles.vehicle import Vehicle
from compounding import inflation


class Portfolio:
    
    def __init__(self, investment_matrix: InvestmentMatrix, vehicles: Optional[dict[str, Vehicle]] = None, starting_cash: float = 0):
        self._investment_matrix = investment_matrix
        self._vehicles = vehicles if vehicles is not None else {}
        self._invest(starting_cash)
    
    @property
    def vehicles(self) -> Iterable[Vehicle]:
        return self._vehicles.values()
    
    @property
    def net_worth(self) -> float:
        return sum(vehicle.current_value for vehicle in self._vehicles.values())

    def pass_month(self, monthly_available_income: float):
        self._invest(monthly_available_income)
        self._pass_time()

    def make_obligatory_pre_tax_payments(self, gross_monthly_income: float) -> float:
        """
        Pay into the each vehicle the amount you have to based on your gross income
        This is probably just the student loan
        Return the total amount paid in obligatory pre tax payments
        """
        total_pre_tax_payment: float = 0
        for vehicle_name, vehicle in self._vehicles.items():
            obligatory_payment = vehicle.get_obligatory_pre_tax_payment(gross_monthly_income)
            leftover_amount = self._pay_into_vehicle(vehicle_name, obligatory_payment)
            actual_payment = obligatory_payment-leftover_amount
            total_pre_tax_payment += actual_payment
        return total_pre_tax_payment

    def _invest(self, amount: float):
        leftover_money: float = 0
        for vehicle_name in self._vehicles:
            vehicle_percentage = self._investment_matrix.get_weightings_for_vehicle_at_current_month(vehicle_name)
            vehicle_specific_amount = amount*vehicle_percentage
            leftover_money += self._pay_into_vehicle(vehicle_name, vehicle_specific_amount)
        if leftover_money > 0:
            self._invest(leftover_money)
    
    def _pay_into_vehicle(self, vehicle_name: str, amount: float) -> float:
        """"
        Pay `amount` into a vehicle"
        Returns the amount of money you were unable to invest (that is now left over)
        """
        try:
            self._vehicles[vehicle_name].invest(amount)
            return 0
        except LoanTerminatedException as loanTerminatedException:
            leftover_money = loanTerminatedException.remaining
            self._investment_matrix.clear_vehicle(vehicle_name)
            return leftover_money
    
    
    def _pass_time(self):
        for vehicle in self._vehicles.values():
            vehicle.pass_month()
    
    def __repr__(self):
        return "\t".join(str(vehicle) for vehicle in self.vehicles) + f"\t\tNet worth: {fmt(self.net_worth)}"

    def can_retire(self):
        needed_amount = inflation.compound(45_000)
        return self.net_worth * 0.04 > needed_amount

class SimulationBoundsExceededException(Exception):
    pass