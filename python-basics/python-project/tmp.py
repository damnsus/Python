import	requests
import pandas as pd
import logging

log = logging.basicConfig(level = logging.INFO, filename = "py_log.log", filemode = "w")

data = requests.get(url = "https://api.bybit.com/v5/market/mark-price-kline")
d = data.json
da = pd.DataFrame(d)
