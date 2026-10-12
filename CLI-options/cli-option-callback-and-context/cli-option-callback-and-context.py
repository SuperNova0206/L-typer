from typing import Annotated
import typer 

app : typer.Typer = typer.Typer()
__version__ : str = "0.1.0"


def version_callback(value : bool) :
    if value :
        print("App version: {}".format(__version__))


def name_validator(value : str) -> str | typer.BadParameter :
    if value != "Camila" :
        raise typer.BadParameter("The only accepted name is \"Camila\"")
    return value


@app.command()
def main(
        name : Annotated[str | None, typer.Option(callback=name_validator)] = None,
        version : Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True)] = None
) -> None : 
    print("Hello {}".format(name))

if __name__ == "__main__" : app()
