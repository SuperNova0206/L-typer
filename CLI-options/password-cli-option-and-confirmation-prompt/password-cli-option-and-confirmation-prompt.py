import typer
from typing import Annotated


# initializing 
app : typer.Typer = typer.Typer()

@app.command()
def main(
    password : Annotated[str, typer.Option(help="User password", rich_help_panel="Required option", prompt=True, confirmation_prompt="Please confirm your password", hide_input=True)]
) -> None : 
    print(f"Your password is : {password}")

if __name__ == "__main__" : app()