from typing import Optional
import requests
import typer

from util.pretty_print import print_table

from . import __app_name__, __version__

app = typer.Typer()
api = "https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL"


@app.command()
def get_price(ticker: str):
    response = requests.get(api)
    title = "Close Price"
    col_name = response.json()["fields"]
    rows = response.json()["data"]
    filtered_rows = [row for row in rows if row[0] == ticker]

    print_table(title, col_name, filtered_rows)


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
