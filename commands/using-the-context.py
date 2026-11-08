import typer 
from typing import Annotated 
import time

# initialzing the app
app = typer.Typer()


@app.command()
def create(
    name : Annotated[str, typer.Argument(help="User name", rich_help_panel="Required argument")],
) -> None :
    print("Creating a user . . .")
    time.sleep(1)
    print("The user {} has beign created".format(name))


# listing the invoked command
@app.callback()
def main(ctx : typer.Context) : 
    print(ctx.invoked_subcommand)


# executable callback
@app.callback(invoke_without_command=True)
def init() -> None :
    print("Initializing database . . .")
    time.sleep(1)
    print("Finished")

if __name__ == "__main__" : app()