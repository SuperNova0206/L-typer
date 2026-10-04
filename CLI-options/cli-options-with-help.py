from typing import Annotated
import typer

# initializing
app : typer.Typer = typer.Typer()


@app.command()
def main_v1(
    name : Annotated[str, typer.Argument(help="User name", rich_help_panel="Required")],
    tel : Annotated[str, typer.Option(help="User telephone 555-555-55", rich_help_panel="Customazition")] = "",
    info : Annotated[bool, typer.Option(help="Displaying user info", rich_help_panel="Customazition", show_default=False)] = False 
) -> None :
    """
    Accepts one required argument "name".
    Two optional arguments --tel --info
    Displays the user information when --info is equala to True
    """
    if info:
        print("User name: {}\nPhone number: {}".format(name, tel))
        return
    print("Hello {}!".format(name))


if __name__ == "__main__" : app()