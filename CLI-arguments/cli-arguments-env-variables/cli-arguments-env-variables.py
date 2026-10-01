from typing import Annotated
import typer 
import getpass

# initiate
app : typer.Typer = typer.Typer()

@app.command()
def main_v1(name : Annotated[str, typer.Argument(envvar="USER_NAME")] = str(getpass.getuser())) -> None : 
    print(f"Hello {name}")


if __name__ == "__main__" : app()