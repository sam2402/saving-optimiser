import time_tracker


class InvestmentMatrix:
    
    def __init__(self, initial_weightings: dict[int, dict[str, int|float]]):
        self._weightings = initial_weightings
    
    @property
    def month_count(self):
        return len(self._weightings)
    
    def clear_vehicle(self, vehicle_name: str):
        for _month_index in range(time_tracker.current_month_index, self.month_count):
            self._weightings[_month_index][vehicle_name] = 0
    
    def get_weightings_for_vehicle_at_current_month(self, vehicle_name: str) -> float:
        monthly_sum = sum(self._weightings[time_tracker.current_month_index].values())
        return self._weightings[time_tracker.current_month_index][vehicle_name]/monthly_sum