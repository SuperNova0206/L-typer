from typer import Typer
from rich.console import Console
from rich.table import Table

console : Console = Console()
app : Typer = Typer()


@app.command()
def data() : 
    table : Table = Table("Name", "Age")
    table.add_row("Rick", "Protal Gun")
    table.add_row("Morty", "Plumbs")
    console.print(table)

    

if __name__ == "__main__" : app()