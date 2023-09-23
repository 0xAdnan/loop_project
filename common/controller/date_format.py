from datetime import datetime


class DateFormatChange:
    def __init__(self, data):
        self.data = data

    def convert_date(self):
        if self.data and "India Standard Time" in self.data:
            new_date = self.data.replace('(India Standard Time)', '').rstrip()
            self.data = datetime.strptime(new_date, '%a %b %d %Y %H:%M:%S %Z%z').strftime(
                "%Y-%m-%d")
        return self.data

    def check_and_convert_date(self, date):
        if not isinstance(date, datetime.datetime):
            if "T" in date:
                date = date.split("T")[0]
            date_result = datetime.datetime.strptime(date, "%Y-%m-%d")
            return date_result
        return date
