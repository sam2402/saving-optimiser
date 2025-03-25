def get_monthly_available_money(month_index: int) -> int:
    yearly_income = (90_000 + 5000*(month_index//12))*(1.025)**(month_index//12)
    return yearly_income/(12*4)
    # return 1000 * 1.1**(month_index//12)