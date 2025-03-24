from income.available_income import get_monthly_available_money
from income.portfolio import Portfolio
from investment_matrix import InvestmentMatrix
from vehicles.pension import Pension
from vehicles.savings import Savings
from vehicles.student_loan import StudentLoan


def simulate_finances(investment_matrix: InvestmentMatrix):
    net_worth_by_month = []
    portfolio = Portfolio(investment_matrix, {"Pension": Pension(), "Savings": Savings(), "Student Loan": StudentLoan()})

    for month_index in range(investment_matrix.month_count):
        available_income_for_month = get_monthly_available_money(month_index)
        portfolio.pass_month(available_income_for_month)
        net_worth_by_month.append(portfolio.net_worth)
    
    print(portfolio._investment_matrix._weightings)
    print(net_worth_by_month[-1])


if __name__ == "__main__":
    investment_matrix = InvestmentMatrix({
        month_index: {
            "Pension": 1,
            "Savings": 1,
            "Student Loan": 10
        } for month_index in range(12*30)
    })
    simulate_finances(investment_matrix) 