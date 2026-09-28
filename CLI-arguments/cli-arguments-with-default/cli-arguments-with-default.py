import random 
import typer
from typing import Annotated

# initializing 
app : typer.Typer = typer.Typer()


def get_name() -> str :
    return random.choice(["Deadpool", "Rick", "Morty", "Hiro"])

@app.command()
def main(name : Annotated[str, typer.Argument(default_factory=get_name)]) :
    print(f"Hello {name}")

if __name__ == "__main__" : app()