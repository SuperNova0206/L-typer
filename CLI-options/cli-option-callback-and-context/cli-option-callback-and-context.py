from typing import Annotated
import typer 

app : typer.Typer = typer.Typer()


def name_validator(ctx : typer.Context, param : typer.CallbackParam, value : str) -> str | typer.BadParameter :
    if ctx.resilient_parsing : return
    print("Validating param: {}".format(param.name))
    if value != "Camila" :
        raise typer.BadParameter("The only accepted name is \"Camila\"")
    return value

@app.command()
def main(name : Annotated[str, typer.Argument(callback=name_validator)]) -> None : 
    print("Hello {}".format(name))

if __name__ == "__main__" : app()
