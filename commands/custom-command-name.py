import typer
from typing import Annotated
from rich import print

# initializing
App  = typer.Typer(
    no_args_is_help=True,
    suggest_commands=True,
    rich_markup_mode="rich"
)


@App.command("create")
def create_a_user(
    name : Annotated[str, typer.Argument(help="User name", rich_help_panel="Required argument")],
    age : Annotated[str, typer.Option(help="User age", rich_help_panel="Reqruied option")],
    is_student : Annotated[str, typer.Option(help="Is he a student", prompt="Is he a student [Y/N]?")] = "n",
    is_working : Annotated[str, typer.Option(help="Is he working" , prompt="Is he working [Y/N]")] = "n"
) -> None :

    # data variable
    data : dict = {
        "name" : name,
        "age" : age,
        "is_student" : False if is_student.lower() == "n" or is_student.lower() == "no" else True,
        "is_working" : False if is_working.lower() == "n" or is_working.lower() == "no" else True
    }

    if data["is_student"] :
        print("Welcome {} :waving_hand:! We're excited to start our journey".format(name))
    elif data["is_working"] :
        print("Welcome {}!".format(name)) 

if __name__ == "__main__" : App()

