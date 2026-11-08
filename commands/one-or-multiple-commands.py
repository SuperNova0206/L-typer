import typer
from typing import Annotated

# initialzing the app
app = typer.Typer(no_args_is_help=True)


@app.command("create")
def create_a_user(
    name : Annotated[str, typer.Argument(help="User name", rich_help_panel="Required argument")]
) -> None :
    print("Hello {}".format(name))


# doc
@app.callback()
def doc() -> None :
    """
    create\t\t[NAME] creating a user
    """

if __name__ == "__main__" : app()
