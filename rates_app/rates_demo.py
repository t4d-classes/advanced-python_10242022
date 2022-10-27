

from datetime import date
from concurrent.futures import ThreadPoolExecutor
from business_days import business_days

import time
import aiohttp
import asyncio
import requests

start_date = date(2020, 8, 1)
end_date = date(2020, 8, 20)
base_currency = 'INR'
currency_symbols = ['USD', 'CAD', 'GBP']

def get_rate_url(business_day):
    return "".join([
        "http://127.0.0.1:5050/api/",
        str(business_day),
        f"?base={base_currency}&symbols=",
        ",".join(currency_symbols)
    ])


def get_rates_sync(start_date, end_date):

    rate_responses = []

    for business_day in business_days(start_date, end_date):
        response = requests.get(get_rate_url(business_day), timeout=60)
        rate_responses.append(response.text)

    return rate_responses
    

def get_rates_thread(start_date, end_date):
    ...

def get_rates_async(start_date, end_date):
    ...

def get_rates_threadpool(start_date, end_date):
    ...


get_rates_funcs = [
    ("Sync", get_rates_sync),
    # ("Thread", get_rates_thread),
    # ("Async", get_rates_async),
    # ("ThreadPool", get_rates_threadpool),
]

for (func_name, get_rates) in get_rates_funcs:

    start_time = time.time()
    print(f"Running {func_name}")

    rates = get_rates(start_date, end_date)

    for rate in rates:
        print(rate)
    end_time = time.time()

    print(f"{func_name} time elapsed: {end_time - start_time}")
