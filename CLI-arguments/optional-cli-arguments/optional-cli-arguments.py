import typer
from typing import Annotated

app : typer.Typer = typer.Typer()


@app.command()
def required(name : Annotated[str, typer.Argument()]) -> None :
    print("Hello {}!".format(name))

@app.command()
def optional(name : Annotated[str, typer.Argument()] = "World") -> None :
    print(f"Hello {name}")


if __name__ == "__main__" : app()