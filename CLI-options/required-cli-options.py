from typing import Annotated
import typer 

# initializing
app : typer.Typer = typer.Typer()

@app.command()
def main_v1(
    name : Annotated[str, typer.Argument(help="User name")],
    lastname : Annotated[str, typer.Option(help="Required option (lastname)")]
) -> None :
    print(f"Hello {name} {lastname}!")

if __name__ == "__main__" : app()