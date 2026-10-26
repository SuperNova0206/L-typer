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
def init( path : Annotated[Path, typer.Option("--path", "-p", help="csv file location", rich_help_panel="Required Option", prompt="Where do you want to locate the file?")]) -> None :
    """
    [green]Initialze the app[/green]\n
    init --path|-p
    """
    success_initialzing_msg : Style = Style(color="bright_white", bgcolor="spring_green3")
    error_initialzing_msg : Style = Style(color="bright_white", bgcolor="bright_red")
    if Path.exists(path) : 
        with open(FILE_LOCATION + FILE_NAME, mode="w") as file : pass
        text.print(":) The app initialized successfully!", style=success_initialzing_msg)
    else : 
        text.print(":( Oops something went wrong!", style=error_initialzing_msg)
        text.print("Default path: {}".format(FILE_LOCATION + FILE_NAME))



@App.command(help="create a user")
def create(
    name : Annotated[str, typer.Argument(
            help="user name", rich_help_panel="Required argument"
        )
    ],
) -> None : 
    user_id : int
    if Path.exists(FILE_LOCATION + FILE_NAME) :
        with open(FILE_LOCATION + FILE_NAME, mode="r") as file : 
            user_id = sum(1 for i in file)
    else : ...



if __name__ == "__main__" : App()

    

