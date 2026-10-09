from typing import Annotated
import typer 
from rich.console import Console

# initializing the app
app : typer.Typer = typer.Typer()
render : Console = Console()

# prompt with a message
@app.command()
def info(
    name : Annotated[str, typer.Argument(help="User name", rich_help_panel="Required argument")],
    lastname : Annotated[str, typer.Option(prompt="Please write your last name", rich_help_panel="Required option")]
) -> None : 
    render.print("Hello ", end="")
    render.print(f"{name} {lastname}", style="blue3")

# confirmation
def confirm(
        name : Annotated[str, typer.Argument(help="User name", rich_help_panel="Required argument")],
        lastname : Annotated[str, typer.Option(help="Last name", rich_help_panel="Required option")],
        tel : Annotated[str, typer.Option(help="User phone number", rich_help_panel="Required option", confirmation_prompt=True, prompt="Please insert your phone number")]
) -> None : 
    render.print("Hello", end="")
    render.print(f" {name} {lastname} ", style="blue3")
    render.print(f"tel : {tel}")
if __name__ == "__main__" : typer.run(confirm)