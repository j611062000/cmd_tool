from rich.console import Console
from rich.table import Table
   

def print_table(title:str, schema:list[str], data:list[list[str]]) -> None:
    table = Table(title=title)

    for col in schema:
        table.add_column(col, justify="right", style="cyan", no_wrap=True)

    for row in data:
        table.add_row(*row)

    console = Console()
    console.print(table)