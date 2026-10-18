import typer 
from typing import Annotated
from rich.console import Console

render : Console = Console()
App : typer.Typer = typer.Typer(
    no_args_is_help=True, 
    rich_markup_mode="rich", 
    help="Awesome CLI user manager.", # What the application 
    suggest_commands=True # suggesting "Did you mean ...?"
)

@App.command(rich_help_panel="CRUD operations")
def create(
    user_name : Annotated[str, typer.Argument(help="User name")]
) -> None :
    """
    [green]Creating a user using his name[/green]\n
    create <THE_NAME>
    """
    if user_name : 
        print("The user {} has created successfully".format(user_name))
        return
    print("We couldn't create the user {} for some reason".format(user_name))


@App.command(rich_help_panel="CRUD operations")
def delete(
    user_id : Annotated[int, typer.Option("--id", rich_help_panel="Rquired option", help="Deleting a user by his id --id 1, 2, . . . ")],
    confirm : Annotated[bool, typer.Option("--confirm", "-c", prompt="Do you wanna delete that user?", help="Confirm your deletion (--confirm|-c True)")] = False
) -> None :
    """
    [red]Deleting a user using his id[/red]\n
    delete --id
    """
    if confirm and user_id > 0 :
        print("The user {} has deleted successfully".format(user_id))
        return
    print("We couldn't delete the user number {}".format(user_id))


# deprecated
@App.command(deprecated=True)
def delete_all(
    confirmation : Annotated[str | None, typer.Option(help="Seeking for a confrimation to delete all the users", rich_help_panel="Required option", prompt="Do you want to delete all the users Y/N?")]
) -> None :
    """
    Deleting all the users at once.\n
    delete-all
    """
    if confirmation.lower() == "y" :
        print("The deletion has been completed")
        return

if __name__ == "__main__" : App()