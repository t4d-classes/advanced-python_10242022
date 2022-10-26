

from datetime import datetime, timedelta, date
import time

# start_time = time.time()

# time.sleep(1)

# end_time = time.time()

# print(end_time - start_time) # wall time


print(datetime.now())

start = datetime.now()

print(start + timedelta(days=180))

# https://www.w3schools.com/python/gloss_python_date_format_codes.asp

print(datetime.now().strftime("%B %A"))

tax_day_str = "04-2022-18"

print(datetime.strptime(tax_day_str, "%m-%Y-%d"))

print(datetime.now().weekday()) # weekday starts on Monday with 0

tax_date = datetime.strptime(tax_day_str, "%m-%Y-%d")

print( (start - tax_date).days ) # number of days since tax day