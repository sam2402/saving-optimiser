from time_tracker import current_month_index


class InvestmentMatrix:
    
    def __init__(self, initial_weightings: dict[int, dict[str, int|float]]):
        self._weightings = initial_weightings
    
    @property
    def month_count(self):
        return len(self._weightings)

    def clear_vehicle(self, vehicle_name: str):
        for _month_index in range(current_month_index, self.month_count):
            self._weightings[_month_index][vehicle_name] = 0
            post_cleared_total = sum(self._weightings[_month_index].values())
            for vehicle_name in self._weightings[_month_index]:
                new_weighting = self._weightings[_month_index][vehicle_name]/post_cleared_total
                self._weightings[_month_index][vehicle_name] = new_weighting
    
    def get_weightings_for_vehicle_at_current_month(self, vehicle_name: str) -> float:
        monthly_sum = sum(self._weightings[current_month_index].values())
        return self._weightings[current_month_index][vehicle_name]/monthly_sum