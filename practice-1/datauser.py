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

@App.command(help="initialize the script")
def init() -> None :
    """
    [green]Initialze the app[/green]\n
    init --path|-p
    """
    success_msg : Style = Style(color="bright_white", bgcolor="green3")
    if Path.exists(FILE_LOCATION + FILE_NAME) : return
    with open(FILE_LOCATION + FILE_NAME, mode="w", newline="") as file : 
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
    if not Path.exists(FILE_LOCATION + FILE_NAME) :
        raise InitializingException(":( Make sure to initialize the script before using any commands use --help")

    # user id
    with open(FILE_LOCATION + FILE_NAME) as file :
      user_id = sum(1 for row in file)
      file.close()


    # writing the user data
    with open(FILE_LOCATION + FILE_NAME, mode="a", newline="") as csvfile :
        writer  = csv.writer(csvfile)
        writer.writerow([user_id, name, age, is_work])

    # rendering the users table
    text.print("The user {} has created successfully!".format(name), style="green3")

# script exceptions 
class InitializingException(Exception) :
    pass
if __name__ == "__main__" : App()

    

