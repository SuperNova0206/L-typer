from typing import Annotated
import typer, csv, os
from rich.console import Console
from rich.style import Style
from rich.table import Table
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
console : Console = Console()
table : Table = Table(title="Users data")

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
        writer.writerow(["_ID", "USER NAME", "USER AGE", "IS WORKING"])
    console.print(":) The app initialized successfully", style=success_msg)

# create
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

    # sucess message
    console.print("The user {} has created successfully!".format(name), style="green3")

# update
@App.command(help="update a user")
def update(
    id : Annotated[int, typer.Option(help="user id", prompt=">>> user id ", rich_help_panel="Required Option")],
    name : Annotated[str | None, typer.Option(help="user name", prompt=">>> User name ")] = None,
    age : Annotated[str | None, typer.Option(help="user age", prompt=">>> User age ")] = None,
    is_working : Annotated[str | None, typer.Option(help="working?", prompt=">>> Is he working Y/N? ")] = "n",
    confirmation : Annotated[str | None, typer.Option(help="user confirmation", prompt=">>> Do you want to update the user Y/N? ")] = "n"
) -> None : 

    header : list
    UpdateData : list

    # read and change data's value
    with open(FILE_LOCATION + FILE_NAME, mode="r", newline="") as csvfile :
        header = csv.DictReader(csvfile).fieldnames
        data = csv.reader(csvfile)
        UpdateData = [item for item in data]

    # changing
    for item in UpdateData : 
        index : int
        if id == int(item[0]) : 
            index = UpdateData.index(item)
            UpdateData[index] = [id, name, age, False if is_working.lower() == "n" or is_working.lower() == "no" else True]


    if confirmation.lower() == "yes" or confirmation.lower() == "y" : 
        # updating
        with open(FILE_LOCATION + FILE_NAME, mode="w", newline="") as file : 
            writer = csv.writer(file)
            writer.writerow(header)
            for item in UpdateData : 
                writer.writerow(item)
            file.close()
        console.print("The user {} updated successfully!".format(id), style="green3")
        return
    console.print("Operation canceled!", style="red3")

# delete
@App.command(help="delete a user")
def delete(
    id : Annotated[int, typer.Option(help="user id", rich_help_panel="Required option")],
    confirmation : Annotated[str, typer.Option(help="confirmation for deleting the user", prompt="Do you want to delete that user [Y/N]? ")] = "n"
) -> None : 
    header : list
    updatedData : list

    # reading 
    with open(FILE_LOCATION + FILE_NAME, mode="r", newline="") as csvfile :
        header = csv.DictReader(csvfile).fieldnames
        data = csv.reader(csvfile)
        updatedData = [item for item in data]

    # deleting the user
    with open(FILE_LOCATION  + FILE_NAME, mode="w", newline="") as csvfile :
        for item in updatedData : 
            if id == int(item[0]) :
                index = updatedData.index(item)
                updatedData.pop(index)

    # rewriting the data
    if confirmation.lower() == "y" or confirmation.lower() == "yes" : 
        with open(FILE_LOCATION + FILE_NAME, mode="w", newline="") as file : 
                    writer = csv.writer(file)
                    writer.writerow(header)
                    for item in updatedData : 
                        writer.writerow(item)
                    file.close()
        console.print("The user {} deleted successfully!".format(id), style="green3")
        return
    console.print("Operation canceled!", style="red3")

@App.command(help="read the data")
def read() -> None :
    header : list
    data : list 

    # reading
    with open(FILE_LOCATION + FILE_NAME, mode="r", newline="") as csvfile : 
        header = csv.DictReader(csvfile).fieldnames
        reader = csv.reader(csvfile)
        data = [item for item in reader]

    # table (header)
    for th in header :
        table.add_column(th, justify="left")

    # table (body)
    for item in data :
        table.add_row(*item)

    console.print(table)
    

# script exceptions 
class InitializingException(Exception) :
    pass
if __name__ == "__main__" : App()

    

