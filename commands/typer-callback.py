import typer
from typing import Annotated


# doc
def documentation() -> None :
    """
        This is a typer callback article test! It's not a documentation 
        or anything.
    """

App : typer.Typer = typer.Typer(callback=documentation, no_args_is_help=True)


@App.command("create", help="[green]create a user[/green]")
def create_a_user(
    name : Annotated[str, typer.Argument(help="User name", rich_help_panel="Required argument")]
) -> None :
    print("The user {} has created with success!".format(name))


if __name__ == "__main__" : App()