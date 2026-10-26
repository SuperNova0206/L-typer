from typing import Annotated
import typer, csv, os
from rich.console import Console
from rich.table import Table
from rich.style import Style
from  pathlib import Path

# CONSTANTS
FILE_LOCATION = './'
FILE_NAME = 'users.csv'

# initializing
App : typer.Typer = typer.Typer(
    no_args_is_help=True,
    help="CLI app for managing users using CRUD operations (create, read, update, delete)",
    suggest_commands=True,
    rich_markup_mode="rich"
)

# styling
text : Console = Console()
table : Table = Table()

@App.command(help="initialize the script")
def init() -> None :
    """
    [green]Initialze the app[/green]\n
    init --path|-p
    """
    success_msg : Style = Style(color="bright_white", bgcolor="green3")
    if Path.exists(FILE_LOCATION + FILE_NAME) : return
    with open(FILE_LOCATION + FILE_NAME, "w") as file : pass
    text.print(":) The app initialized successfully", style=success_msg)


@App.command(help="create a user")
def create(
    name : Annotated[str, typer.Argument(
            help="user name", rich_help_panel="Required argument"
        )
    ],
) -> None : 
    user_id : int
    with open(FILE_LOCATION + FILE_NAME) as file : 
        user_id = sum(1 for i in file) + 1

    
if __name__ == "__main__" : App()

    

