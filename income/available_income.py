def get_monthly_available_money(month_index: int) -> int:
    return 1000 * 1.1**(month_index//12)