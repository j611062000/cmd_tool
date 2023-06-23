import typer
import requests
import pickle
import os

from typing import Optional
from model.daily_price import DailyPrice, DailyPriceList, Ticker, get_daily_price_list
from util.pretty_print import print_table
from . import __app_name__, __version__, config_instance

# todo: add a class for response

app = typer.Typer()
api = "https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL"
local_cache_dir = "./price_getter/.cache"
sync_pirce_local_cache = "closing_price.pickle"
config_instacne = config_instance

def __try_get_price_from_cache(is_from_cache: bool = True) -> DailyPriceList:
    full_cache_path = local_cache_dir+"/"+sync_pirce_local_cache
    price_by_ticker = dict[Ticker, DailyPrice]()

    if is_from_cache and os.path.exists(full_cache_path):
        with open(full_cache_path, "rb") as infile:
            print("reading from cache...")
            price_by_ticker = pickle.load(infile)
    else:
        if os.path.exists(full_cache_path): os.remove(full_cache_path)
        
        response = requests.get(api)
        price_by_ticker = get_daily_price_list(response)
        print("reading from API...")
        sync_pirce_to_local(price_by_ticker)
    
    return price_by_ticker

@app.command("refresh")
def get_price(ticker: str = ""):
    daily_price_list: DailyPriceList = __try_get_price_from_cache(config_instacne.is_enable_cache)
    
    title = "Close Price" + ", Updated at: " + daily_price_list.date

    print_table(title, daily_price_list, ticker)


def sync_pirce_to_local(daily_price_list: DailyPriceList):
    isExist = os.path.exists(local_cache_dir)
    if not isExist:
        os.makedirs(local_cache_dir)

    with open(local_cache_dir+"/"+sync_pirce_local_cache, "wb") as outfile:
        pickle.dump(daily_price_list, outfile)

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
