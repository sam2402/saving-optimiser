from income.income import Income
from portfolio import Portfolio
from investment_matrix import InvestmentMatrix
import time_tracker
from vehicles.pension import Pension
from vehicles.savings import Savings
from vehicles.student_loan import StudentLoan

YEARS = 30

def simulate_finances(investment_matrix: InvestmentMatrix):
    net_worth_by_month = []
    starting_cash = 13_500
    portfolio = Portfolio(investment_matrix, {"Pension": Pension(), "Savings": Savings(), "Student Loan": StudentLoan()}, starting_cash)
    income = Income(portfolio)

    while time_tracker.current_month_index < YEARS*12:
        print(str(portfolio))
        remaining_income_form_month = income.pass_month()
        portfolio.pass_month(remaining_income_form_month)
        net_worth_by_month.append(portfolio.net_worth)
        time_tracker.pass_month()
    
    print(net_worth_by_month[::12])
    # print(investment_matrix._weightings)


if __name__ == "__main__":
    investment_matrix = InvestmentMatrix({
        month_index: {
            "Pension": 0,
            "Savings": 1,
            "Student Loan": 0
        } for month_index in range(12*YEARS)
    })
    simulate_finances(investment_matrix)
    