import typer
from typing import Annotated
import rich

App : typer.Typer = typer.Typer(rich_markup_mode="rich", no_args_is_help=True)

@App.command()
def create(
    user_name : Annotated[str | None, typer.Argument(help="Create a user")]
    ) -> bool :
    """
    [green]Create[/green] a user. 
    """
    if user_name : 
        return True
    return False

@App.command()
def delete(
    user_id : Annotated[int, typer.Option("--id", help="Delete a user", prompt="Do you really want to delete that user?", rich_help_panel="Required option")]
) -> bool :
    """
    [red]Delete[/red] a user.
    """
    if user_id > 0 :
        return True
    return False

if __name__ == "__main__" : App()