from rich.console import Console
from rich.table import Table

from model.daily_price import DailyPriceList, Ticker,DailyPrice
   

def print_table(title:str, p: DailyPriceList, filter: Ticker = "") -> None:
    table = Table(title=title)

    for col in p.schema:
        table.add_column(col, justify="right", style="cyan", no_wrap=True)

    filtered_price: list[DailyPrice] = []
    if filter == "" in p.price_by_ticker: filtered_price = list(p.price_by_ticker.values())
    elif filter in p.price_by_ticker: filtered_price = [p.price_by_ticker[filter]]


    for row in filtered_price:
        table.add_row(row.ticker,
                      row.name,
                      str(row.total_shares),
                      str(row.total_amount),
                      str(row.open),
                      str(row.high),
                      str(row.low),
                      str(row.close),
                      str(row.delta),
                      str(row.total_orders),
                      row.trading_date)

    console = Console()
    console.print(table)