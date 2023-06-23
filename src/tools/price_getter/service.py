import typer
import requests
import pickle
import os

from typing import Optional
from util.pretty_print import print_table
from . import __app_name__, __version__

app = typer.Typer()
api = "https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL"
local_cache_dir = "./price_getter/.cache"
sync_pirce_local_cache = "closing_price.pickle"

def __try_get_price_from_cache(is_from_cache: bool = True):
    response = None
    full_cache_path = local_cache_dir+"/"+sync_pirce_local_cache

    if is_from_cache and os.path.exists(full_cache_path):
        with open(full_cache_path, "rb") as infile:
            print("reading from cache...")
            response = pickle.load(infile)
    else:
        print("reading from API...")
        response = requests.get(api)
    
    return response

@app.command("refresh")
def get_price(ticker: str = "", from_cache: bool = True):
    response = __try_get_price_from_cache(from_cache)
    
    title = "Close Price" + ", Updated at: " + response.json()["date"]
    col_name = response.json()["fields"]
    rows = response.json()["data"]
    filtered_rows = [row for row in rows if row[0] == ticker]

    print_table(title, col_name, filtered_rows if ticker else rows)


@app.command("sync")
def sync_pirce():
    isExist = os.path.exists(local_cache_dir)
    if not isExist:
        os.makedirs(local_cache_dir)

    response = requests.get(api)
    with open(local_cache_dir+"/"+sync_pirce_local_cache, "wb") as outfile:
        pickle.dump(response, outfile)

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
