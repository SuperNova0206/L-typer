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
    with open(FILE_LOCATION + FILE_NAME, "w") as file : 
        writer = csv.writer(file)
        writer.writerow(["_ID", "USER NAME", "USER AGE", "WORKING?"])
    text.print(":) The app initialized successfully", style=success_msg)


@App.command(help="create a user")
def create(
    name : Annotated[str, typer.Argument(
            help="User name", rich_help_panel="Required argument"
        ) 
    ],
    age : Annotated[int, typer.Argument(help="User age", rich_help_panel="Required argument")],
    is_work : Annotated[bool, typer.Option("-w", help="Is the user working", rich_help_panel="Option")] = False,
) -> None : 
    user_id : int
    if Path.exists(FILE_LOCATION + FILE_LOCATION) : 
        with open(FILE_LOCATION + FILE_NAME, mode="a") as file : 
            user_id = sum(1 for i in file) + 1
            writer = csv.writer(file)
            writer.writerow([user_id, name, age, is_work])
    else : 
        raise Exception(":( We're missing some files please run the command \"datause init\"")


    
if __name__ == "__main__" : App()

    

