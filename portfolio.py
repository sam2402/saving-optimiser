from investment_matrix import InvestmentMatrix
from vehicles.loan import LoanTerminatedException
from vehicles.vehicle import Vehicle


class Portfolio:
    
    def __init__(self, investment_matrix: InvestmentMatrix, vehicles: dict[str, Vehicle] = None, starting_cash: int = 0):
        self._investment_matrix = investment_matrix
        self._vehicles = vehicles if vehicles is not None else {}
        self._invest(starting_cash)
    
    @property
    def vehicles(self) -> list[Vehicle]:
        return self._vehicles.values() 
    
    @property
    def net_worth(self) -> int:
        return sum(vehicle.current_value for vehicle in self._vehicles.values())

    def pass_month(self, monthly_available_income: int):
        self._invest(monthly_available_income)
        self._pass_time()
    
    def pay_into_vehicle(self, vehicle_name: int, amount: int):
        try:
            self._vehicles[vehicle_name].invest(amount)
        except LoanTerminatedException as loanTerminatedException:
            leftover_money = loanTerminatedException.remaining
            self._investment_matrix.clear_vehicle(vehicle_name)
            self._invest(leftover_money)
    
    def _invest(self, amount: int):
        leftover_money = 0
        for vehicle_name in self._vehicles:
            try:
                vehicle_percentage = self._investment_matrix.get_weightings_for_vehicle_at_current_month(vehicle_name)
                vehicle_specific_amount = amount*vehicle_percentage
                self._vehicles[vehicle_name].invest(vehicle_specific_amount)
            except LoanTerminatedException as loanTerminatedException:
                leftover_money += loanTerminatedException.remaining
                self._investment_matrix.clear_vehicle(vehicle_name)
        if leftover_money > 0:
            self._invest(leftover_money)
    
    def _pass_time(self):
        for vehicle in self._vehicles.values():
            vehicle.pass_month()
    
    def __repr__(self):
        return ", ".join(str(vehicle) for vehicle in self.vehicles)

class SimulationBoundsExceededException(Exception):
    pass