from requests import Response
Ticker = str

class DailyPrice():
    def __init__(self, ticker: Ticker, 
                 name: str, 
                 total_shares: int, 
                 total_amount: int,
                 open: float,
                 high: float,
                 low: float,
                 close: float,
                 delta: float,
                 total_orders: int,
                 trading_date: str) -> None:
        self.ticker = ticker
        self.name = name
        self.total_shares = total_shares
        self.total_amount = total_amount
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.delta = delta
        self.total_orders = total_orders
        self.trading_date = trading_date

class DailyPriceList():
    def __init__(self, schema: list[str], price_by_ticker: dict[Ticker, DailyPrice], date: str) -> None:
        self.schema: list[str] = schema
        self.price_by_ticker: dict[Ticker, DailyPrice] = price_by_ticker
        self.date: str = date
    

def get_daily_price_list(r: Response) -> DailyPriceList:
    if r.status_code != 200:
        raise Exception("HTTP response code is not 200")
    else:
        response_json = r.json()
        date = response_json["date"]
        price_by_ticker =  {row[0]: DailyPrice(ticker=row[0], 
                                   name=row[1], 
                                   total_shares=row[2], 
                                   total_amount=row[3], 
                                   open=row[4], 
                                   high=row[5], 
                                   low=row[6], 
                                   close=row[7], 
                                   delta=row[8], 
                                   total_orders=row[9], 
                                   trading_date=date) 
                for row in response_json["data"]}

        return DailyPriceList(schema=response_json["fields"], price_by_ticker=price_by_ticker, date=date)