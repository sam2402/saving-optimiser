from compounding import Compounding, inflation
from constants import EMPLOYER_PENSION_MATCH, GRADUATION_DATE, INFLATION_RATE, INTEREST_RATE, INVESTMENT_RETURN_RATE, STARTING_CASH, SIMULATION_YEARS, STUDENT_LOAN_PRINCIPLE, fmt
from income.income import Income, Salary
from portfolio import Portfolio
from investment_matrix import InvestmentMatrix
import time_tracker
from vehicles.pension import Pension
from vehicles.savings import Savings
from vehicles.student_loan import StudentLoan

def simulate_finances(investment_matrix: InvestmentMatrix):
    net_worth_by_month = []
    portfolio = Portfolio(investment_matrix, {
        "Pension": Pension(Compounding(INVESTMENT_RETURN_RATE), EMPLOYER_PENSION_MATCH, 3_147),
        "Savings": Savings(Compounding(INVESTMENT_RETURN_RATE)),
        "Student Loan": StudentLoan(Compounding(INTEREST_RATE), STUDENT_LOAN_PRINCIPLE, GRADUATION_DATE)
    }, STARTING_CASH)
    income = Income(portfolio)

    while time_tracker.current_month_index < SIMULATION_YEARS*12:
        if time_tracker.current_month_index%12 == 0: 
            print(f"Year {time_tracker.current_year_index()}: Salary: {fmt(inflation.adjusted(Salary._get_current_gross_yearly_income()))}\t{str(portfolio)}")
        remaining_income_from_month = income.pass_month()
        portfolio.pass_month(remaining_income_from_month)
        net_worth_by_month.append(portfolio.net_worth)
        time_tracker.pass_month()
    
    print(f"Net worth in {SIMULATION_YEARS} years: {fmt(net_worth_by_month[-1])}")
    inflation_adjusted_net_worth = inflation.adjusted(net_worth_by_month[-1])
    print(f"Inflation adjusted net worth: {fmt(inflation_adjusted_net_worth)}")

if __name__ == "__main__":
    investment_matrix = InvestmentMatrix({
        month_index: {
            "Pension": 1,
            "Savings": 1,
            "Student Loan": 0
        } for month_index in range(12*SIMULATION_YEARS)
    })
    simulate_finances(investment_matrix)
    