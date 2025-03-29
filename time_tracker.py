from datetime import datetime, timedelta
from constants import DAYS_IN_MONTH


current_month_index = 0
current_date = datetime.now()

def pass_month():
    global current_month_index
    global current_date
    current_month_index += 1
    current_date += timedelta(days=DAYS_IN_MONTH)

def current_year_index():
    return current_month_index//12 