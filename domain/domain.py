from datetime import date


# Domain class for calculating employee working years
class EmployeeDomain:
    def __init__(self, name: str, date_of_joining: date):
        self.name = name
        self.date_of_joining = date_of_joining

    # Method for calculating working years
    def calculate_time_period(self) -> int:
        today = date.today()
        working_year = today.year - self.date_of_joining.year - (
                (today.month, today.day) < (self.date_of_joining.month, self.date_of_joining.day))
        return working_year
