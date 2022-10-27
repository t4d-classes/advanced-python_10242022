from datetime import date, timedelta
import holidays

def business_days(start_date, end_date):
    """ business days """

    us_holidays = holidays.UnitedStates()

    for day in range((end_date - start_date).days + 1):
        the_date = start_date + timedelta(day)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            yield the_date


print(f"business days: {__name__}")

if __name__ == "__main__":
    for business_day in business_days(date(2022, 6, 3), date(2022, 7, 5)):
        print(business_day)