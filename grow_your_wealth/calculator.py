from .utils import currencify as cy

def get_growth_records(data):
    """
    Instead of writing too much code in the views file
    we instead implement everything here
    data is a dict of the form
    {'initial_amount': ['500000.00'], 'top_up': ['250000.00'], 'interest_rate': ['0.15'], 'duration_in_years': ['10'], 'topup_frequency': ['month'], 'company': ['Mansa-X'], 'name': ['retirement']}
    investment_class is the Capital class
    """
    name = 'some investment'
    worth = float(data.initial_amount)
    top_up = float(data.top_up)
    freq = data.topup_frequency
    company = data.company
    interest_rate = float(data.interest_rate)
    duration_in_years = int(data.duration_in_years)
    growth_records = Capital(name=name, worth=worth, top_up=top_up, top_up_frequency=freq, company=company)
    growth_records.calculate_growth(yearly_interest_rate=interest_rate,
                               duration_in_years=duration_in_years)
    return growth_records.gains

class Capital:
    """
    A capital class
    """
    def __init__(self, name, worth, top_up, top_up_frequency, company):
        """
        init function
        """
        self.name = name
        self.worth = worth
        self.initial_capital = worth
        self.top_up = top_up
        self.top_up_frequency = top_up_frequency
        self.company = company
        self.duration = None
        self.interest_rate = None
        self.gains = []
    
    def __repr__(self):
        return f'{self.name} capital investment worth Kes {cy(self.initial_capital)} has been invested in {self.company}'
    
    def calculate_growth(self, yearly_interest_rate, duration_in_years):
        """
        Our capital can grow at a yearly interest rate
        yearly interest rate: in decimal e.g 0.1 instead of 10%
        duration_in_years: int e.g. 2
        """
        interest_earned = 0
        for year in range(duration_in_years):
            if self.top_up_frequency == "month":
                for imon in range(12):
                    self.gains.append({"year": year+1,
                                       "month": imon+1,
                                       "interest": interest_earned,
                                       "capital_gains": self.worth})
                    self.worth += self.top_up
            interest_earned = yearly_interest_rate * self.worth
            self.worth += interest_earned
            self.duration = duration_in_years
            self.interest_rate = yearly_interest_rate
            # print(f'Year {year+1}: Interest earned: Kes {cy(interest_earned)}. New capital: Kes {cy(self.worth)}')




if __name__ == "__main__":
    name = "jul2025"
    worth = 250_000
    top_up = 250_000
    freq = "month"
    company = "Mansa-X"
    interest_rate = .18
    duration_in_years = 5
    cap = Capital(name=name, worth=worth, top_up=top_up, top_up_frequency=freq, company=company)
    cap.calculate_growth(yearly_interest_rate=interest_rate,
                               duration_in_years=duration_in_years)

